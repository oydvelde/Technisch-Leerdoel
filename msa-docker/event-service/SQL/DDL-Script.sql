USE MASTER
GO

DROP DATABASE IF EXISTS [EventService-DB]
GO

CREATE DATABASE [EventService-DB]
GO

USE [EventService-DB]
GO

CREATE TABLE Event (
    eventID     INT             PRIMARY KEY     IDENTITY,
    eventName   VARCHAR(255)    NOT NULL
);
