import json, os, pathlib, subprocess, sys, tempfile, unittest
from ssh_option_witness.core import run

CASES = [({'host': 'a.dev', 'config': 'Host *.dev\n User x\nHost *\n User y\n'}, {'values': {'user': 'x'}}), ({'host': 'bad.dev', 'config': 'Host *.dev !bad.dev\n User x\nHost *\n User y\n'}, {'values': {'user': 'y'}}), ({'host': 'a.dev', 'config': 'User global\nHost a.dev\n User local\n'}, {'values': {'user': 'global'}}), ({'host': 'A.DEV', 'config': 'Host *.dev\n Port=2222\n'}, {'values': {'port': '2222'}}), ({'host': 'a', 'config': 'IdentityFile one\nHost *\n IdentityFile two\n'}, {'values': {'identityfile': ['one', 'two']}}), ({'host': 'a', 'config': 'User "two words" # note\n'}, {'values': {'user': 'two words'}}), ({'host': 'a', 'config': 'Host !a\n User denied\n'}, {'values': {}}), ({'host': 'a', 'config': 'Include file\n'}, 'error'), ({'host': 'a', 'config': 'Match all\n'}, 'error'), ({'host': 'a', 'config': 'Port 65536\n'}, 'error'), ({'host': 'a', 'config': 'ProxyCommand touch x\n'}, 'error'), ({'host': 'a', 'config': 'Host [ab]\n User x\n'}, 'error')]

class ContractTests(unittest.TestCase):
    def test_cli_demo(self):
        r=subprocess.run([sys.executable,"-c","from ssh_option_witness.cli import main; raise SystemExit(main())","example.json"],text=True,capture_output=True)
        self.assertEqual(r.returncode,0,r.stderr)
        self.assertIsInstance(json.loads(r.stdout),dict)

    def test_cli_malformed(self):
        with tempfile.TemporaryDirectory() as d:
            path=pathlib.Path(d)/"bad.json";path.write_text("[broken")
            r=subprocess.run([sys.executable,"-c","from ssh_option_witness.cli import main; raise SystemExit(main())",str(path)],text=True,capture_output=True)
            self.assertEqual(r.returncode,2)
            self.assertEqual(r.stdout,"")
            self.assertIn("input error",r.stderr)

def make_case(data,expected):
    def test(self):
        before=json.dumps(data,sort_keys=True)
        if expected=="error":
            with self.assertRaises(ValueError): run(data)
        else:
            result=run(data)
            if expected=="opaque":
                self.assertEqual(set(result["paths"]),{"d","d/new","other"})
                self.assertEqual(result["whiteouts"][0]["removed"],["d/a"])
            elif expected=="order":
                self.assertEqual([r["start"] for r in result["requests"]],[50,0])
                self.assertEqual(result["coverage"],[[0,9],[50,59]])
            else:
                for key,value in expected.items(): self.assertEqual(result[key],value)
        self.assertEqual(json.dumps(data,sort_keys=True),before,"input mutated")
    return test
for i,(data,expected) in enumerate(CASES):
    setattr(ContractTests,"test_contract_%02d"%i,make_case(data,expected))

if __name__=="__main__": unittest.main()
