from dotenv import load_dotenv
import os

def main():

    ### Load env-vars from `.env`
    load_dotenv()


    ### Main job
    # os.system('python get_all_tweets.py')
    os.system('python get_works.py')


if __name__ == "__main__":
    main()