import requests
from skimage import io
import matplotlib.pyplot as plt
import webbrowser

# Ler Chave do arquivo key

with open("key.json", "r") as file:
    linha = file.read().strip()

API_KEY = linha.split("=")[1]

print("CHAVE:", API_KEY)

# Foto do Dia 

url = "https://api.nasa.gov/planetary/apod"

params = {
    "api_key": API_KEY
}

response = requests.get(url, params=params)

print("\nSTATUS CODE APOD:", response.status_code)

print("\nRESPOSTA APOD:")
print(response.text)

# transforma resposta em json
data = response.json()

print("\nTITULO:")
print(data["title"])

print("\nCOPYRIGHT:")
print(data.get("copyright", "Sem copyright"))

print("\nEXPLICAÇÃO:")
print(data["explanation"])

# Limites da api

print("\nLIMITE TOTAL:")
print(response.headers.get("X-RateLimit-Limit"))

print("\nLIMITE RESTANTE:")
print(response.headers.get("X-RateLimit-Remaining"))

# Mostrar imagem ou video 

if data["media_type"] == "image":

    image_url = data.get("hdurl", data.get("url"))

    print("\nABRINDO IMAGEM...")
    print(image_url)

    img = io.imread(image_url)

    plt.figure(figsize=(10, 10))
    plt.imshow(img)
    plt.title(data["title"])
    plt.axis("off")
    plt.show()

else:

    print("\nO conteúdo do dia não é uma imagem.")
    print("Tipo:", data["media_type"])

    # pega o id do vídeo
    video_id = data["url"].split("/embed/")[1].split("?")[0]

    # monta link normal do youtube
    video_url = f"https://www.youtube.com/watch?v={video_id}"

    print("\nABRINDO VÍDEO:")
    print(video_url)

    webbrowser.open(video_url)

# Manifesto

rover_name = "Curiosity"

manifest_url = (
    f"https://api.nasa.gov/mars-photos/api/v1/manifests/{rover_name.lower()}"
)

print("\nURL MANIFEST:")
print(manifest_url)

params = {
    "api_key": API_KEY
}

response = requests.get(manifest_url, params=params)

print("\nSTATUS MANIFEST:")
print(response.status_code)

print("\nRESPOSTA MANIFEST:")
print(response.text)

# transforma em json

manifest_data = response.json()

photo_manifest = manifest_data["photo_manifest"]

max_sol = photo_manifest["max_sol"]
max_date = photo_manifest["max_date"]

print("\nMAX SOL:")
print(max_sol)

print("\nMAX DATE:")
print(max_date)

# Fotos rover

photos_url = (
    f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover_name}/photos"
)

page = 1

camera_choices = ["NAVCAM", "FHAZ", "RHAZ"]

while True:

    params = {
        "api_key": API_KEY,
        "sol": max_sol,
        "page": page
    }

    response = requests.get(photos_url, params=params)

    print(f"\nSTATUS PAGE {page}:")
    print(response.status_code)

    data = response.json()

    photos = data["photos"]

    # se não houver mais fotos
    if len(photos) == 0:

        print(f"\nFim das páginas na página {page}")
        break

    print(f"\nPágina {page} - {len(photos)} fotos")

    for photo in photos:

        camera_name = photo["camera"]["name"]

        # filtra câmeras desejadas
        if camera_name in camera_choices:

            image_url = photo["img_src"]

            print(
                f"\nMostrando imagem | "
                f"ID: {photo['id']} | "
                f"Câmera: {camera_name}"
            )

            try:

                img = io.imread(image_url)

                plt.figure(figsize=(8, 8))

                plt.imshow(img)

                plt.title(
                    f"Página {page} | "
                    f"Câmera: {camera_name} | "
                    f"ID: {photo['id']}"
                )

                plt.axis("off")

                plt.show()

            except Exception as e:

                print("Erro ao carregar imagem:")
                print(e)

    page += 1