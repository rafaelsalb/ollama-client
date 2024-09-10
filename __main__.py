import argparse
import pprint
import sys
import chat.chat
from config import Config
import ping
from dotenv import load_dotenv # type: ignore
import service.generate

load_dotenv()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='cli',
        description='tools for talking to an ollama server through the cli',
    )
    parser.add_argument(
        '--ping',
        action='store_true'
    )
    parser.add_argument(
        '--prompt',
        type=str,
        action='store'
    )
    parser.add_argument(
        '--chat',
        action='store_true'
    )
    args = parser.parse_args()

    if args.ping:
        res = ping.ping()
        print(res)
        sys.exit(0)

    if args.prompt:
        prompt = args.prompt
        res: dict = service.generate.generate({
            "prompt": prompt
        })
        pprint.pprint(res)
        sys.exit(0)

    if args.chat:
        chat.chat.chat()
