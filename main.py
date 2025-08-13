from data_loader import load_and_clean_data
from model import train_and_test
def main():
    df=load_and_clean_data('diabetes.txt')
    train_and_test(df)
if __name__ == '__main__':
    main()
