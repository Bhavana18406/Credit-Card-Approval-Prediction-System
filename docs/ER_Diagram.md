
# Entity Relationship Diagram (ERD)

## Overview

This document describes the data model for the AI-Powered Credit Card Approval System.

## Entities

### 1. Applicant
Represents a credit card applicant.

| Attribute               | Type         | Description                                |
|------------------------|--------------|--------------------------------------------|
| applicant_id           | Integer      | Unique identifier for the applicant        |
| gender                 | String       | Gender of the applicant (M/F)              |
| age                    | Integer      | Age of the applicant                       |
| owns_car               | Boolean      | Indicates if applicant owns a car          |
| owns_property          | Boolean      | Indicates if applicant owns property       |
| children_count         | Integer      | Number of children                         |
| annual_income          | Float        | Annual income of the applicant             |
| employment_status      | String       | Current employment status                  |
| education_level        | String       | Highest education level achieved           |
| marital_status         | String       | Marital status of the applicant            |
| dwelling_type          | String       | Type of residence                          |
| employment_length      | Integer      | Years of employment                        |
| has_mobile_phone       | Boolean      | Indicates if has mobile phone              |
| has_work_phone         | Boolean      | Indicates if has work phone                |
| has_phone              | Boolean      | Indicates if has phone                     |
| has_email              | Boolean      | Indicates if has email                     |
| job_title              | String       | Job title (if applicable)                  |
| family_member_count    | Integer      | Total family members                       |
| account_age            | Float        | Age of account (days)                      |

### 2. Prediction
Represents a credit card approval prediction.

| Attribute               | Type         | Description                                |
|------------------------|--------------|--------------------------------------------|
| prediction_id          | Integer      | Unique identifier for the prediction       |
| applicant_id           | Integer      | Foreign key to Applicant                   |
| prediction_timestamp   | DateTime     | When the prediction was made               |
| is_approved            | Boolean      | Prediction result (approved/rejected)      |
| confidence_score       | Float        | Confidence of the prediction (0-100)       |
| risk_score             | Float        | Calculated risk score (0-100)              |
| credit_eligibility     | String       | Eligibility tier (Low/Medium/High)         |

## Relationships

- An **Applicant** can have one or more **Predictions** (1-to-many relationship)
