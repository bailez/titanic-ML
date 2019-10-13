using DataFrames, CSV
test = CSV.read("/run/media/bailez/Dados/Projetos e Serviços/titanic-resolutions/data/test.csv");
print(test);
print(head(test))
print("\n",typeof(test))