from setuptools import setup

with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")

setup(
    name="SyntaxAutoFix",
    packages=["SyntaxAutoFix"],
    entry_points={
        "console_scripts": ['syntaxautofix = SyntaxAutoFix.syntaxalert:main']
    },
    install_requires=[
          'keyboard',
      ],
    version=0.1,
    description="description",
    long_description=long_descr,
    author="SOMEONE",
    author_email="INSERTEXT@gmail.com",
    url="http://url.com",
    include_package_data=True
)
