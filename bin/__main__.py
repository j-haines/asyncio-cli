#! /usr/bin/env python3

import asyncio
import sys
from argparse import ArgumentParser, Namespace


def parse_args() -> Namespace:
    parser = ArgumentParser("{%PROJECT_NAME%}")

    return parser.parse_args()


async def main(opts: Namespace) -> int:
    print("Hello, world!")

    return 0


if __name__ == "__main__":
    opts = parse_args()
    loop = asyncio.get_event_loop()

    sys.exit(loop.run_until_complete(main(opts)))