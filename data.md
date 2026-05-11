## What is Salesforce?

[Salesforce Official Website](https://www.salesforce.com/?utm_source=chatgpt.com)

Salesforce is a **cloud-based CRM (Customer Relationship Management) platform**.
It helps companies manage:

* Customers
* Sales
* Marketing
* Customer support
* Business automation
* Analytics

Instead of installing software on company servers, Salesforce runs completely on the cloud (SaaS — Software as a Service).

Think of it as a central system where a company stores and manages all customer-related activities.

---

# Why Companies Use Salesforce

Suppose a company gets leads from websites, emails, calls, and ads.

Without Salesforce:

* Data is scattered in Excel sheets
* Teams don't communicate properly
* Leads get lost
* Follow-ups are missed

With Salesforce:

* Everything is stored in one place
* Sales team tracks customers
* Managers see reports
* Automation reduces manual work
* Customer support becomes organized

---

# Main Uses of Salesforce

## 1. Sales Management (Sales Cloud)

Used by sales teams.

Features:

* Lead tracking
* Opportunity management
* Contact management
* Sales forecasting
* Pipeline tracking

Example:
A company can track:

* Who is interested
* Which deals are pending
* Expected revenue

---

## 2. Customer Support (Service Cloud)

Used by support teams.

Features:

* Ticket management
* Chat support
* Case tracking
* Knowledge base
* AI support tools

Example:
When a customer complains, Salesforce creates a “Case” and tracks resolution.

---

## 3. Marketing Automation (Marketing Cloud)

Used for:

* Email campaigns
* SMS campaigns
* Customer journeys
* Personalized marketing

Example:
Automatic birthday emails to customers.

---

## 4. App Development

Salesforce is also a development platform.

Developers can build:

* Business apps
* Custom workflows
* Internal tools
* Portals

without managing servers.

---

## 5. Automation

Salesforce automates repetitive tasks.

Examples:

* Auto email when lead is created
* Auto approval process
* Task reminders
* Workflow automation

---

# What is Apex?

Apex is Salesforce’s **programming language**.

It is similar to:

* Java
* C#

Used to write:

* Business logic
* Automation
* Database operations
* APIs
* Triggers

---

# Why Apex is Needed

Salesforce has many no-code tools.

But sometimes companies need custom logic.

Example:

> “When an Opportunity becomes Closed Won, automatically create an invoice.”

This requires programming → Apex.

---

# Features of Apex

## Strongly Typed

Variables must have data types.

Example:

```apex
Integer age = 25;
String name = 'Sarthak';
```

---

## Object-Oriented

Supports:

* Classes
* Objects
* Inheritance
* Interfaces

---

## Database Integrated

Apex directly works with Salesforce database using SOQL.

Example:

```apex
List<Account> accs = [SELECT Id, Name FROM Account];
```

---

# What is an Apex Class?

An Apex class is like a blueprint containing methods and logic.

Example:

```apex
public class HelloWorld {

    public static void sayHello() {
        System.debug('Hello Salesforce');
    }
}
```

---

# How to Create an Apex Class

## Method 1 — Using Developer Console

### Steps

1. Login to Salesforce
2. Open:

   * Gear Icon → Developer Console
3. Go to:

   * File → New → Apex Class
4. Enter class name
5. Write code
6. Save

---

## Example Apex Class

```apex
public class StudentManager {

    public static void showMessage() {
        System.debug('Welcome to Apex');
    }
}
```

---

# Calling the Class

Open:

* Debug → Open Execute Anonymous Window

Run:

```apex
StudentManager.showMessage();
```

---

# Apex Access Modifiers

| Modifier  | Meaning                |
| --------- | ---------------------- |
| public    | Accessible everywhere  |
| private   | Only inside class      |
| global    | Accessible outside org |
| protected | Parent-child access    |

---

# What is a Trigger in Apex?

Triggers execute automatically when data changes.

Example:

* Before Insert
* After Update
* Before Delete

Example trigger:

```apex
trigger AccountTrigger on Account(before insert) {

    for(Account acc : Trigger.new) {
        acc.Description = 'New Customer';
    }
}
```

---

# What is Lightning in Salesforce?

Lightning is Salesforce’s **modern UI framework and component-based platform**.

Old UI:

* Salesforce Classic

New UI:

* Lightning Experience

---

# Why Lightning Was Introduced

Classic UI was:

* Old-looking
* Less interactive
* Harder to customize

Lightning provides:

* Faster UI
* Modern design
* Reusable components
* Mobile-friendly apps

---

# Parts of Lightning

## 1. Lightning Experience

Modern Salesforce interface.

Features:

* Better dashboards
* Kanban views
* Interactive pages

---

## 2. Lightning Components

Reusable UI components.

Like:

* Buttons
* Forms
* Tables
* Charts

---

## 3. Lightning Web Components (LWC)

Modern frontend framework.

Built using:

* HTML
* JavaScript
* CSS

This is the current recommended technology.

---

# Example LWC Structure

```text
helloWorld/
 ├── helloWorld.html
 ├── helloWorld.js
 ├── helloWorld.js-meta.xml
```

---

# Simple LWC Example

### HTML

```html
<template>
    <h1>Hello Salesforce</h1>
</template>
```

### JavaScript

```javascript
import { LightningElement } from 'lwc';

export default class HelloWorld extends LightningElement {

}
```

---

# Aura vs LWC

| Aura             | LWC              |
| ---------------- | ---------------- |
| Older framework  | Modern framework |
| Slower           | Faster           |
| Complex          | Easier           |
| Uses Aura syntax | Standard JS      |

Today companies prefer:

* LWC

---

# Does Salesforce Have a Database?

Yes.

Salesforce stores huge amounts of customer data.

But users do NOT directly manage databases like traditional systems.

Salesforce handles:

* Storage
* Scaling
* Security
* Backups

automatically.

---

# Which Database Does Salesforce Use?

Salesforce uses:

* Oracle Database (historically and heavily)
* Proprietary distributed systems internally

The exact architecture is highly customized by Salesforce.

---

# How Salesforce Data is Structured

Salesforce works with:

* Objects
* Records
* Fields

Similar to:

| Salesforce | Database |
| ---------- | -------- |
| Object     | Table    |
| Record     | Row      |
| Field      | Column   |

---

# Standard Objects

Built-in objects:

| Object      | Purpose            |
| ----------- | ------------------ |
| Account     | Company            |
| Contact     | Person             |
| Lead        | Potential customer |
| Opportunity | Sales deal         |
| Case        | Support ticket     |

---

# Custom Objects

Companies can create their own objects.

Example:

* Student
* Hospital
* Employee

---

# Querying Data in Salesforce

Salesforce uses:

## SOQL (Salesforce Object Query Language)

Similar to SQL.

Example:

```apex
SELECT Name FROM Account
```

---

# SOQL Example in Apex

```apex
List<Account> accs =
    [SELECT Id, Name FROM Account];

System.debug(accs);
```

---

# Important Salesforce Technologies

| Technology  | Purpose               |
| ----------- | --------------------- |
| Apex        | Backend programming   |
| LWC         | Frontend UI           |
| SOQL        | Query language        |
| Flow        | No-code automation    |
| Trigger     | Event automation      |
| Visualforce | Older UI framework    |
| API         | External integrations |

---

# Real-World Salesforce Workflow Example

Imagine an e-commerce company:

1. Customer fills form
2. Lead created in Salesforce
3. Salesperson gets notification
4. Opportunity created
5. Deal closed
6. Invoice generated automatically
7. Support team handles issues

All managed inside Salesforce.

---

# Career Roles in Salesforce

| Role                  | Work               |
| --------------------- | ------------------ |
| Salesforce Admin      | Configure platform |
| Salesforce Developer  | Write Apex/LWC     |
| Salesforce Consultant | Business solutions |
| Salesforce Architect  | System design      |
| Salesforce QA         | Testing            |

---

# Why Salesforce Is Popular

* Cloud-based
* Highly customizable
* Secure
* Huge ecosystem
* Low infrastructure maintenance
* Strong enterprise adoption

Large companies worldwide use Salesforce for CRM and automation.

---

# Recommended Learning Path

## Beginner

* CRM basics
* Salesforce Admin basics
* Objects & Fields
* Flow

## Intermediate

* SOQL
* Apex
* Triggers
* LWC

## Advanced

* Integrations
* APIs
* Security
* Architecture

---

# Official Learning Platform

[Salesforce Trailhead](https://trailhead.salesforce.com/?utm_source=chatgpt.com)

Trailhead is the best free platform to learn Salesforce practically.

```java
public class Lab {

    public static void method1() {

        Integer a = 10;
        Integer b = 20;

        System.debug('Sum of ' + a + ' + ' + b + ' = ' + (a + b));
    }
}

```
```java
public class AllOps {
	    public static void operations() {

        Integer a = 20;
        Integer b = 10;
        System.debug('Addition = ' + (a + b));
        System.debug('Subtraction = ' + (a - b));        
        System.debug('Multiplication = ' + (a * b));
        System.debug('Division = ' + (a / b));
    }
}
```
```java
public class Table {
	    public static void displayTable() {
        Integer num = 5;
        for(Integer i = 1; i <= 10; i++) {
            System.debug(num + ' x ' + i + ' = ' + (num * i));
        }
    }
}
```