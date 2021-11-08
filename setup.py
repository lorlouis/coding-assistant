import setuptools
# source: https://shobhitgupta.medium.com/how-to-publish-your-own-pip-package-560bde836b17  # noqa
# this file was shamelessly stolen and then modified to fit
# this projet's needs

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="my_package",
    version="0.0.1",
    author="Louis Sven Goulet",
    author_email="louis dot sven at gmail dot com",
    description=(
        "Recreate the joys of Office Assistant from "
        "the comfort of the Python interpreter"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lorlouis/coding-assistant",
    packages=setuptools.find_packages(),
    install_requires=['sys'],
    classifiers=[
        "Programming Language :: Python :: 3",
        # TODO find a license
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
