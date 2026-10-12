import fnmatch, shlex

SCALARS={"hostname","user","port","batchmode","connecttimeout","serveraliveinterval","identitiesonly"}
ADDITIVE={"identityfile"}

def run(data):
    host,text=data.get("host"),data.get("config")
    if not isinstance(host,str) or not host or len(host)>253 or any(c.isspace() for c in host) or not isinstance(text,str) or len(text)>100000:
        raise ValueError("bounded host and configuration required")
    active=True
    values,trace={},[]
    for line,raw in enumerate(text.splitlines(),1):
        words=shlex.split(raw,comments=True)
        if not words:
            continue
        if "=" in words[0]:
            key,value=words[0].split("=",1)
            words=[key,value]+words[1:]
        elif len(words)>=2 and words[1]=="=":
            words=words[:1]+words[2:]
        key=words[0].lower()
        args=words[1:]
        if key=="host":
            if not args or any(x=="!" or "[" in x or "]" in x for x in args):
                raise ValueError("Host patterns required")
            pos=[x for x in args if not x.startswith("!")]
            neg=[x[1:] for x in args if x.startswith("!")]
            active=any(fnmatch.fnmatchcase(host.lower(),x.lower()) for x in pos) and not any(fnmatch.fnmatchcase(host.lower(),x.lower()) for x in neg)
            trace.append({"line":line,"keyword":"host","matched":active})
            continue
        if key not in SCALARS|ADDITIVE or len(args)!=1:
            raise ValueError("unsupported directive or arity on line "+str(line))
        value=args[0]
        if key=="port" and (not value.isascii() or not value.isdigit() or not 1<=int(value)<=65535):
            raise ValueError("invalid port")
        if key in {"batchmode","identitiesonly"} and value.lower() not in {"yes","no"}:
            raise ValueError("yes/no required")
        if key in {"connecttimeout","serveraliveinterval"} and (not value.isascii() or not value.isdigit()):
            raise ValueError("nonnegative integer timeout required")
        if not active:
            reason="host_not_matched"
        elif key in ADDITIVE:
            values.setdefault(key,[]).append(value)
            reason="appended"
        elif key in values:
            reason="earlier_value_wins"
        else:
            values[key]=value
            reason="selected"
        trace.append({"line":line,"keyword":key,"reason":reason})
    return {"host":host,"values":dict(sorted(values.items())),"trace":trace}
