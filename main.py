import pandas as pd
import os

from git.repo.base import Repo


def download_repository(url: str, name: str):
    return Repo.clone_from(url, f'{name}')


if __name__ == '__main__':
    df = pd.read_csv("fil.csv")
    os.chdir('projects')
    for index, col in df.iterrows():
        download_repository(col["Link til Github repository"], col['E-post (studentmail)'])
