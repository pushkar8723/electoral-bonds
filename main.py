import tabula

dfs = tabula.read_pdf('data/purchaser.pdf', pages='all')
tabula.convert_into("data/purchaser.pdf", "output/purchase.csv", output_format="csv", pages='all')

dfs = tabula.read_pdf('data/encasher.pdf', pages='all')
tabula.convert_into("data/encasher.pdf", "output/encash.csv", output_format="csv", pages='all')