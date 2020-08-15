import os, random

def main():
    spiders = os.listdir('worker/spiders')[1:]
    os.system(f"scrapy crawl {random.choice(spiders).split('.')[0]} ")

if __name__ == "__main__":
    while True:
        main()