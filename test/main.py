import argparse
import sys

from alexandria_markup.client.alexandria_markup import AlexandriaMarkup


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--server", dest="server", help='Base URI of Alexandria server')
    args = parser.parse_args(argv)
    print("ARGS:", args)

    alexandria = AlexandriaMarkup(args.server)
    about = alexandria.about().json
    # assert about['version'] == 'develop'
    print("ABOUT:", about)

    documents = alexandria.documents

    lmnl_in = '[text}[p=p-1}This is a simple paragraph.{p=p-1]{text]'
    doc_id = documents.add(lmnl_in).uuid

    lmnl_out = documents.lmnl(doc_id)
    print("LMNL out:", lmnl_out)
    # assert lmnl_out == lmnl_in

    latex1 = documents.document_latex(doc_id)
    assert latex1 is not None
    print("Document LaTeX:", latex1)

    latex2 = documents.kdtree_latex(doc_id)
    assert latex2 is not None
    print("k-d tree LaTeX:", latex2)

    latex3 = documents.markupdepth_latex(doc_id)
    assert latex3 is not None
    print("markup-depth LaTeX:", latex3)

    latex4 = documents.matrix_latex(doc_id)
    assert latex4 is not None
    print("text/markup matrix LaTeX:", latex4)

    lmnl_in2 = '[lmnl}text{lmnl]'
    documents.set(doc_id, lmnl_in2)

    lmnl_out2 = documents.lmnl(doc_id)
    assert lmnl_out2 == lmnl_in2
    print("LMNL (2):", lmnl_out2)

if __name__ == "__main__":
    main(sys.argv[1:])
