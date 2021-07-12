from setuptools import setup

with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")

setup(
    name="SyntaxAutoFix",
    packages=["SyntaxAutoFix"],
    entry_points={
        "console_scripts": ['syntaxautofix = SyntaxAutoFix.syntaxautofix:main']
    },
    install_requires=[
          'keyboard',
      ],
    version="2.5.0",
    description="Autofix your typos on Linux easily!",
    long_description=long_descr,
    long_description_content_type='text/markdown',
    author="Mte90",
    author_email="mte90net@gmail.com",
    url="https://github.com/Mte90/SyntaxAutoFix",
    include_package_data=True
)
