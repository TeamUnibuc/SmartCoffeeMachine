## Unit testing
For unit testing we used the python library `unittest`. To run the tests, execute the commands:
```
make unit-test
```

## Integration testing
We wrote a test to check that the HTTP server is starting and its connection to the database. This test works using the same `unittest` library and can be executed with `make integration-test`. We wrote more comprehensive integration tests in the `integration.py` file. Executing it requires that the docker containers are already running and running the file.


## Bug identification

As recommended, we used the Microsoft [Restler](https://github.com/microsoft/restler-fuzzer) tool with the following output

```
Starting task Test...
Using python: 'python3' (Python 3.10.2)
Request coverage (successful / total): 7 / 7
No bugs were found.
Task Test succeeded.
Collecting logs...
```



To reproduce, follow these stepts:

1. Install .NET 5.0 from [here](https://docs.microsoft.com/en-us/dotnet/core/install/linux?WT.mc_id=dotnet-35129-website)

2. Download the official repo
```sh
git clone https://github.com/microsoft/restler-fuzzer.git && cd restler-fuzzer
```

3. Create the folder for the Restler binaries
```sh
mkdir ../restler_bin
```

4. Build the Restler project
```sh
python3 ./build-restler.py --dest_dir ../restler_bin
```

5. Compile it
```sh
cd ../restler_bin
dotnet ./restler/Restler.dll compile --api_spec ../SmartCoffeeMachine/openapi.json
```

6. Run it
```sh
cd Compile
dotnet ./restler/Restler.dll test --grammar_file grammar.py --dictionary_file dict.json --settings engine_settings.json --no_ssl
```
