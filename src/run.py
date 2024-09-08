from modeling.prediction import prediction
from warnings import filterwarnings
filterwarnings("ignore")


def main():
    current_price = (input("Baz Fiyatı Giriniz: "))
    target_price = prediction(current_price)
    print(target_price)


if __name__ == "__main__":
   while True:
        main()
            