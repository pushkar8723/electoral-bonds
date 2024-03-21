import tabula

dfs = tabula.read_pdf('data/purchase-full-disclosure.pdf', pages='all')
tabula.convert_into("data/purchase-full-disclosure.pdf", "output/purchase-full-disclosure.csv", output_format="csv", pages='all')

dfs = tabula.read_pdf('data/encashed-full-disclosure.pdf', pages='all')
tabula.convert_into("data/encashed-full-disclosure.pdf", "output/encashed-full-disclosure.csv", output_format="csv", pages='all')