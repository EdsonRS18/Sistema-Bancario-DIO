from setuptools import setup, find_packages

setup(
    name="meu_banco",
    version="0.1.0",
    description="Projeto de banco em Python",
    author="Edson_RS",
    author_email="edsongomesjr21@gmail.com",
    packages=find_packages(),
    include_package_data=True,  
    install_requires=[
        # Dependências do projeto
    ],
    package_data={
        'banco': ['../assets/*.png'],  # Inclui a imagem no pacote
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
