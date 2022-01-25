# SmartCoffeeMachine

[![CI](https://github.com/TeamUnibuc/SmartCoffeeMachine/actions/workflows/coverage.yml/badge.svg)](https://github.com/TeamUnibuc/SmartCoffeeMachine/actions/workflows/coverage.yml)

## Start The Project

 * Install `Docker` and `Docker-Compose`.
 * Naviate in the root of the project.
 * Run `$ docker-compose up -d`.

## Intro

As the name suggests, this is the brain for a smart coffee machine capable of supplying personalized drink recommendations.

The project is implemented as part of an university assignment by:
 * Chichirim Stelian
 * Dragancea Constantin
 * Moroianu Theodor
 * Puscasu Felix

The functional requirements are described [here](wiki/analiza_cerintelor.md).

A full implementation overview and documentation is located in the wiki, [here](wiki/wiki.md).

Useful links:
* [drive](https://drive.google.com/drive/u/0/folders/1iyG4vzVHs1718v1f8eSRSbOx5QOlbnQM)
* [FastAPI](https://fastapi.tiangolo.com/)
* [FastMQTT](https://pypi.org/project/fastapi-mqtt/)
* [OpenAPI](https://www.openapis.org/)
* [AsyncAPI](https://www.asyncapi.com/)

## Evaluare

 * 1 punct  - Oficiu.
 * 9 puncte - Programul realizat.

### Cerinte (2.5p)

 * Expune un Rest API HTTP – documentat folosind Open API (Swagger) 
 * Expune un API MQTT – documentat folosind AsyncAPI
 * Aplicația să aibă minim 5 funcționalități – puteți să vă gândiți la ele ca sell points ale aplicației. Depinde de aplicația pe care v-ați propus să o faceți, dar chestii de genul o funcționalitate e scăderea, o altă funcționalitate e adunarea, nu înseamnă chiar că sunt diferite 
 * Tot ce faceți să se găsească într-un singur repo.

### Alte Cerinte

 * Toate funcționalitățile și/sau toate endpoints au unit teste asociate. +1.5p
 * Documentația de analiză este up to date + 1p
 * Documentația de utilizare reflectă aplicația reală + 1p

### Alte Cerinte

 * Sa prelucram date reale. 1p
 * Tool de detectare automata a bug-urilor 1.5p
 * Integration tests 1p
 * Coverage >80% a testelor 0.5
