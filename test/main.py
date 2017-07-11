"""
   Copyright 2017 Huygens ING

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import argparse
import sys
import json

from alexandria_markup.client.alexandria_markup import AlexandriaMarkup

def print_divider():
    print("\n--------------------------------------------------------------------------------\n")

def log(label,obj):
    print_divider()
    print("== ",label,": ==\n",obj)

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--server", dest="server", help='Base URI of Alexandria server')
    args = parser.parse_args(argv)
    log("ARGS", args)

    alexandria = AlexandriaMarkup(args.server)
    about = alexandria.about().json
    # assert about['version'] == 'develop'
    log("ABOUT", about)

    documents = alexandria.documents

    lmnl_in = '[text}[p=p-1}This is überhaupt a very simple paragraph.{p=p-1]{text]'
    doc_id = documents.add_from_lmnl(lmnl_in).uuid

    lmnl_out = documents.lmnl(doc_id)
    log("LMNL out", lmnl_out)
    # assert lmnl_out == lmnl_in

    latex1 = documents.document_latex(doc_id)
    assert latex1 is not None
    log("Document LaTeX", latex1)

    latex2 = documents.kdtree_latex(doc_id)
    assert latex2 is not None
    log("k-d tree LaTeX", latex2)

    latex3 = documents.markupdepth_latex(doc_id)
    assert latex3 is not None
    log("markup-depth LaTeX", latex3)

    latex4 = documents.matrix_latex(doc_id)
    assert latex4 is not None
    log("text/markup matrix LaTeX", latex4)

    result = documents.query(doc_id, "select text from markup where name='text'")
    assert result is not None
    # print("result (object):",result);
    log("result (values)",result["values"]);

    lmnl_in2 = '[lmnl}text{lmnl]'
    documents.set_from_lmnl(doc_id, lmnl_in2)

    lmnl_out2 = documents.lmnl(doc_id)
    assert lmnl_out2 == lmnl_in2
    log("LMNL (2)", lmnl_out2)

if __name__ == "__main__":
    main(sys.argv[1:])
