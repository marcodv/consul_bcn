# Spring Boot Shopping Cart Web App

## About

This is a demo project for practicing Spring + RESTful. The idea was to build some API for a basic shopping cart web app.

It was made using **Spring Boot**, **Spring Data JPA**, **Spring Data REST** and **Docker**. 
Database is in memory **H2**.

Based on: https://github.com/reljicd/spring-boot-shopping-cart

## Configuration

### Configuration Files

Folder **src/resources/** contains config files for **shopping-cart** Spring Boot application.

* **src/resources/application.properties** - main configuration file. Here it is possible to change admin username/password,
as well as change the port number.

## How to run

There are several ways to run the application. You can run it from the command line with Maven or Docker. 

Once the app starts, go to the web browser and visit `http://localhost:8070/swagger-ui.html` (SwaggerUI interface)

Other URLs:

- Health check: http://localhost:8070/health

### Maven

Open a terminal and run the following commands to ensure that you have valid versions of Java and Maven installed:

```bash
$ java -version
java version "1.8.0_102"
Java(TM) SE Runtime Environment (build 1.8.0_102-b14)
Java HotSpot(TM) 64-Bit Server VM (build 25.102-b14, mixed mode)
```

```bash
$ mvn -v
Apache Maven 3.3.9 (bb52d8502b132ec0a5a3f4c09453c07478323dc5; 2015-11-10T16:41:47+00:00)
Maven home: /usr/local/Cellar/maven/3.3.9/libexec
Java version: 1.8.0_102, vendor: Oracle Corporation
```

#### Using the Maven Plugin

The Spring Boot Maven plugin includes a run goal that can be used to quickly compile and run your application. 
Applications run in an exploded form, as they do in your IDE. 
The following example shows a typical Maven command to run a Spring Boot application:
 
```bash
$ mvn spring-boot:run
``` 

#### Using Executable Jar

To create an executable jar run:

```bash
$ mvn clean package
``` 

To run that application, use the java -jar command, as follows:

```bash
$ java -jar target/shopping-cart-0.0.1-SNAPSHOT.jar
```

To exit the application, press **ctrl-c**.

### Docker

It is possible to run **shopping-cart** using Docker:

Build Docker image:

```bash
$ mvn clean package
$ docker build -t poc-consul/app -f docker/Dockerfile .
```

Run, Stop, Start Docker container:
```bash
$ docker run -d -p 8070:8070 --name poc-consul-app poc-consul/app
$ docker logs -f poc-consul-app
$ docker stop poc-consul-app
$ docker start poc-consul-app
```

## Docker 

Folder **docker** contains:

* **docker/Dockerfile** - Docker build file for executing shopping-cart Docker image. 
Instructions to build artifacts, copy build artifacts to docker image and then run app on proper port with proper configuration file.

## Tests

Tests can be run by executing following command from the root of the project:

```bash
$ mvn test
```

### H2 Database web interface

Go to the web browser and visit `http://localhost:8070/h2-console`

In field **JDBC URL** put

```
jdbc:h2:mem:shopping_cart_db
```

In `/src/main/resources/application.properties` file it is possible to change both
web interface url path, as well as the datasource url.
