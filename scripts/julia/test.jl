using DataFrames, CSV
test = CSV.read("/run/media/bailez/Dados/Projetos e Serviços/titanic-ML/data/test.csv")
train = CSV.read("/run/media/bailez/Dados/Projetos e Serviços/titanic-ML/data/train.csv")
survived = train[:Survived]
deletecols!(train,[:Name,:Ticket,:Cabin ])
deletecols!(test,[:Name,:Ticket,:Cabin ])
print(head(train), "\n", head(test))