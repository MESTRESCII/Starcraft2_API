from running import Running


def main():
    print('Running Api')
    teste = Running()
    teste.run_api()
    print('Getting Token')
    teste.run_token()
    print('Building Tables')
    teste.run_grandmaster()
    teste.run_refactor_json()
    print('Refactoring Tables')
    teste.run_normalize_json()
    teste.run_refactor_table()
    teste.run_build_new_table()
    print('America Table')
    teste.run_table_generatorAM()
    print('Europe Table')
    teste.run_table_generatorEU()
    print('Korea Table')
    teste.run_table_generatorKR()
    print('Done!')


if __name__ == "__main__":
    main()
