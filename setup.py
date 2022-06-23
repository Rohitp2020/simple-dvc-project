from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="Rohitp2020",
    description="A small package for dvc ml pipeline demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Rohitp2020/simple-dvc-project.git",
    author_email="rohitpunetha2001@gmail.com",
    # package_dir={"":"src"},
    # packages=find_packages(where="src"),licence="GNU",
    python_requires=">=3.6",
    packages=["src"],
    licence="GNU",
    install_requires=[
        'dvc',
        'dvc[gdrive]',
        'dvc[s3]',
        'pandas',
        'scikit-learn'
    ]
)