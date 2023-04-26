import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

print(*[filename.split(".")[0] for filename in os.listdir("./opinions")], sep ="\n")

product_code = input("Podaj kod produktu: ")
opinions = pd.read_json(f"./opinions/{product_code}.json")
opinions.stars = opinions.stars.map(lambda x: float(x.split("/")[0].replace(",",".")))


#wyliczanie podstawowych statystyk
opinions_count = opinions.opinion_id.count()
#
pros_count = opinions.pros.map(bool).sum()
cons_count = opinions.cons.map(bool).sum()
stars_avg = opinions.stars.mean().round(2)
print(f"""Dla produktu o kodzie {product_code} 
pobrano {opinions_count} opinii.
Dla {pros_count} podano liste zalet,
a dla {cons_count} podano liste wad. 
Srednia ocena produktu wynosi {stars_avg}.""")

if not os.path.exists("./plots"):
    os.mkdir("./plots")

#histogram czestosci poszcegolnych ocen
stars = opinions.stars.value_counts().reindex(list(np.arange(0,5.5,0.5)), fill_value=0)
print(stars)
stars.plot.bar()
plt.title("Histogram gwiazdek")
plt.savefig(f"./plots/{product_code}_stars.png")
plt.close()



recomendations = opinions.recommendation.value_counts(dropna=False)
recomendations.plot.pie(label="", autopct="%1.1f%%")
plt.savefig(f"./plots/{product_code}_recommendations.png")
plt.show()