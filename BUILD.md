
### Test

Run the following and ensure that all the tests are executing successfully.

```sh
cd JuspayECLibrary/JuspayECLibrary
python Test.py
```

### Build & Push the binary to PyPi

Decide the new version number for the project. Update `setup.py` with this new version number. Run the following command from the Project home directory.

```sh
cd JuspayECLibrary
python setup.py sdist
twine upload dist/*
```
> You will be prompted for the password to upload the distribution to PyPi. For password, please contact ec@juspay.in.
