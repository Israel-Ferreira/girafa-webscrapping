import csv
import os

from datetime import datetime


def create_folder_if_not_exists(folder_path: str, filename="prices.csv"):
    if not os.path.isdir(folder_path):
        os.mkdir(folder_path)
    else:
        os.remove(os.path.join(folder_path, filename))

    


def write_products_csv(produtos):
    formatted_date = datetime.now().strftime("%d-%m-%Y")

    path_csv = f"prices/{formatted_date}"


    create_folder_if_not_exists(path_csv)


    with open(f"{path_csv}/prices.csv", "w") as file:
        field_names =  ["nome", "preco", "link_site"]

        writer = csv.DictWriter(file, fieldnames=field_names)

        writer.writeheader()

        for produto in produtos:
            writer.writerow({"nome": produto.nome, "preco": produto.preco, "link_site": produto.link_site})