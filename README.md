# QAOps TP --- Automated Testing & Software Quality

## 1. Project Overview

This project was developed as part of the **Projet de Fin de Module :
Automatisation des Tests et Qualité Logicielle** at **Université Hassan2 --- Faculté des Sciences Aïn Chock**.

The objective is to build a practical QAOps workflow covering the main
stages of software quality assurance:

- Functional UI testing
- REST API testing
- Performance testing
- Security testing
- Continuous Integration / Continuous Testing
- Automated test reporting

The project combines Selenium, Pytest, Postman/Newman, Apache JMeter,
OWASP ZAP, Jenkins, Docker, and Allure.

---

## 2. Project Objectives

The project follows the assignment requirements and focuses on five main
testing areas:

---

Area Tool / Technology Objective

---

UI Testing Selenium + Pytest Automate functional
tests on the Formy web
application

API Testing Postman + Newman Validate REST API
operations using Reqres

Performance Testing Apache JMeter Evaluate response time,
throughput, and error
rate

Security Testing OWASP ZAP Identify common web
security weaknesses

CI/CD Jenkins + Docker Automatically execute
UI and API tests in a
pipeline

Reporting Allure + JUnit Produce readable
automated test reports

---

---

# 3. Test Strategy

The testing strategy is based on the following workflow:

```text
                    QAOps Pipeline
                         |
          +--------------+--------------+
          |                             |
     UI Testing                    API Testing
   Selenium/Pytest               Postman/Newman
          |                             |
          +--------------+--------------+
                         |
                  Automated Reports
                  JUnit / Allure
                         |
          +--------------+--------------+
          |                             |
   Performance Testing            Security Testing
       Apache JMeter                 OWASP ZAP
          |                             |
          +--------------+--------------+
                         |
                    Jenkins CI/CD
                         |
                  Docker Environment
```

The objective is not only to execute tests manually, but to integrate
automated testing into a repeatable CI/CD workflow.

---

# 4. Project Structure

```text
QA-OPS-TP/
│
├── JMeter/
│   ├── image.png
│   └── image1.png
│
├── api-tests/
│   ├── image.png
│   └── postman/
│       └── QAOps_Collection.postman_collection.json
│
├── docs/
│   └── test-plan.md
│
├── security/
│   ├── 2026-10-06-ZAP-Report-.html
│   └── 2026-10-06-ZAP-Report-/
│
├── ui-tests/
│   ├── conftest.py
│   ├── pytest.ini
│   ├── requirements.txt
│   ├── image.png
│   │
│   ├── pages/
│   │   ├── base_page.py
│   │   └── formy_page.py
│   │
│   └── tests/
│       ├── test_formy.py
│       └── test_setup.py
│
├── .gitignore
└── README.md
```

The project follows the **Page Object Model (POM)** for Selenium tests,
separating page locators/actions from test cases.

---

# 5. UI Testing --- Selenium + Pytest

## 5.1 Objective

The UI testing phase automates functional scenarios on the **Formy** web
application.

The tests verify that important user-interface components behave as
expected.

## 5.2 Implemented Scenarios

The following scenarios were automated:

---

ID Scenario Expected Result

---

UI-01 Open Formy homepage Homepage loads
successfully

UI-02 Fill complete web form Form fields accept the
expected values

UI-03 Select radio button Radio button becomes
selected

UI-04 Select dropdown option Expected option is
selected

UI-05 Handle JavaScript alert Alert is detected and
accepted

---

The modal scenario was initially investigated but was removed from the
final automated suite.

## 5.3 Page Object Model

The UI tests use a Page Object Model architecture.

### `BasePage`

Contains reusable Selenium operations such as:

- Opening URLs
- Finding elements
- Clicking elements
- Entering text

### `FormyPage`

Contains:

- Formy URLs
- Page locators
- Form interactions
- Dropdown operations
- Radio button operations

This approach keeps test cases readable and makes locator maintenance
easier.

## 5.4 Example Test Execution

The tests can be executed with:

```bash
cd ui-tests

pip install -r requirements.txt

pytest tests -v
```

For Allure results:

```bash
pytest tests -v --alluredir=../reports/allure-results
```

## 5.5 Selenium Environment

The Jenkins environment uses Chromium/ChromeDriver in headless mode so
that Selenium tests can run without a graphical desktop.

The browser configuration includes:

```text
--headless=new
--no-sandbox
--disable-dev-shm-usage
--window-size=1920,1080
```

---

# 6. API Testing --- Postman + Newman

## 6.1 Objective

The API testing phase validates REST API operations using the **Reqres**
API.

The Postman collection is stored in:

```text
api-tests/postman/QAOps_Collection.postman_collection.json
```

## 6.2 Implemented Requests

ID HTTP Method Endpoint Expected Status

---

API-01 GET `/users?page=2` 200
API-02 POST `/users` 201
API-03 PUT `/users/{user_id}` 200
API-04 DELETE `/users/{user_id}` 204

The collection validates both HTTP status codes and response content
where applicable.

## 6.3 Newman Execution

The collection can be executed from the command line using:

```bash
newman run api-tests/postman/QAOps_Collection.postman_collection.json
```

In Jenkins, Newman is executed automatically as part of the CI pipeline.

JUnit output is generated for Jenkins:

```bash
newman run api-tests/postman/QAOps_Collection.postman_collection.json \
  --reporters cli,junit \
  --reporter-junit-export reports/api-tests.xml
```

---

# 7. Performance Testing --- Apache JMeter

## 7.1 Objective

The performance testing phase evaluates the Reqres API under concurrent
load.

The assignment requires at least 50 users executing GET and POST
operations.

The implemented test generated:

- 50 GET requests
- 50 POST requests
- 100 total samples

The main metrics analyzed were:

- Average response time
- Minimum response time
- Maximum response time
- Error rate
- Throughput

## 7.2 Results

### GET Users

Metric Result

---

Samples 50
Average 199 ms
Minimum 165 ms
Maximum 404 ms
Error Rate 0.0%
Throughput 1.01694/sec

### POST User

Metric Result

---

Samples 50
Average 118 ms
Minimum 89 ms
Maximum 226 ms
Error Rate 0.22%
Throughput 1.02218/sec

### Overall

Metric Result

---

Total Samples 100
Average 159 ms
Minimum 89 ms
Maximum 404 ms
Error Rate 0.11%
Throughput 2.02897/sec

## 7.3 Analysis

The POST operation had a lower average response time than the GET
operation:

```text
GET  = 199 ms
POST = 118 ms
```

The GET test recorded no errors, while the POST test recorded a very
small error rate of **0.22%**.

Across all 100 requests, the overall error rate was **0.11%**.

The maximum observed response time was **404 ms**, which occurred during
the GET test.

These results indicate that the tested API remained responsive during
the executed test scenario, with a very low overall error rate.

---

# 8. Security Testing --- OWASP ZAP

## 8.1 Objective

OWASP ZAP was used to perform a security scan against the Formy web
application.

The objective was to identify common web application security weaknesses
and provide recommendations.

The generated ZAP report is stored under:

```text
security/
```

## 8.2 Detected Findings

The scan identified the following alert categories:

Finding Occurrences / Scope

---

Absence of Anti-CSRF Tokens Detected
Content Security Policy Header Not Set Systemic
Sub Resource Integrity Attribute Missing 4
Vulnerable JS Library Detected
Cookie Without Secure Flag Systemic
Cookie without SameSite Attribute Systemic
Cross-Domain JavaScript Source File Inclusion 3
Strict-Transport-Security Header Not Set Systemic
Timestamp Disclosure - Unix Systemic
X-Content-Type-Options Header Missing 5
Information Disclosure - Suspicious Comments 13
Modern Web Application Systemic
Re-examine Cache-control Directives Systemic
Session Management Response Identified 19

## 8.3 Recommendations

### Anti-CSRF Tokens

State-changing requests should use anti-CSRF protections where
applicable.

### Content Security Policy

A suitable `Content-Security-Policy` header should be configured to
reduce the impact of cross-site scripting and unauthorized resource
execution.

### Subresource Integrity

External JavaScript resources should use SRI attributes where
appropriate:

```html
<script
  src="https://example.com/script.js"
  integrity="..."
  crossorigin="anonymous"
></script>
```

### Secure Cookies

Cookies containing sensitive information should use:

```text
Secure
HttpOnly
SameSite
```

according to the application's requirements.

### HTTP Security Headers

The application should consider configuring:

```text
Strict-Transport-Security
X-Content-Type-Options
Content-Security-Policy
```

### JavaScript Dependencies

Third-party JavaScript libraries should be regularly updated and checked
for known vulnerabilities.

### Information Disclosure

Suspicious comments and unnecessary technical information should be
removed from production resources.

### Cache-Control

Caching directives should be reviewed to ensure sensitive responses are
not incorrectly cached.

---

# 9. CI/CD --- Jenkins

## 9.1 Objective

The CI/CD phase integrates automated UI and API tests into Jenkins.

The objective is to ensure that automated tests can be executed
consistently whenever the pipeline runs.

## 9.2 Jenkins Environment

Jenkins runs inside Docker.

The custom Jenkins image provides the tools required by the QA pipeline:

```text
Jenkins
Docker CLI
Docker Compose
Python 3
pip
Node.js
npm
Newman
Chromium
ChromeDriver
Allure Commandline
```

This avoids installing the complete testing environment directly on the
host machine.

## 9.3 Pipeline Stages

The Jenkins pipeline follows this structure:

```text
Checkout
   |
   v
Prepare Environment
   |
   v
Install UI Dependencies
   |
   v
Selenium UI Tests
   |
   v
Newman API Tests
   |
   v
Generate Allure Report
   |
   v
Publish / Archive Reports
```

## 9.4 UI Test Stage

The Selenium tests generate:

```text
reports/ui-tests.xml
reports/allure-results/
```

The JUnit XML file can be consumed directly by Jenkins.

## 9.5 API Test Stage

Newman generates:

```text
reports/api-tests.xml
```

This allows Jenkins to display API test results alongside the UI
results.

## 9.6 Allure Reporting

Pytest uses the `allure-pytest` plugin to generate Allure test result
files.

Example:

```bash
pytest ui-tests/tests \
    -v \
    --alluredir=reports/allure-results
```

The Jenkins pipeline can then generate the HTML report:

```bash
allure generate \
    reports/allure-results \
    -o reports/allure-html \
    --clean
```

The generated report provides a visual overview of:

- Passed tests
- Failed tests
- Test duration
- Test suites
- Test steps
- Test descriptions
- Test severity
- Test execution details

---

# 10. Jenkins Test Reports

The pipeline generates JUnit reports for Jenkins:

```text
reports/
├── ui-tests.xml
├── api-tests.xml
├── allure-results/
└── allure-html/
```

The reports are archived by Jenkins so that test results remain
available after pipeline execution.

Security reports are also archived:

```text
security/
```

This makes the pipeline execution reproducible and provides evidence of
the performed QA activities.

---

# 11. Continuous Testing Workflow

The final QAOps workflow can be summarized as:

```text
Developer Push
      |
      v
   Jenkins
      |
      v
   Checkout
      |
      +----------------------+
      |                      |
      v                      v
 Selenium UI             Newman API
      |                      |
      +----------+-----------+
                 |
                 v
          Automated Reports
                 |
        +--------+--------+
        |                 |
        v                 v
      JUnit            Allure
        |
        v
   Jenkins Results
```

Performance testing with JMeter and security testing with OWASP ZAP are
maintained as dedicated QA activities and their evidence is stored in
the repository.

---

# 12. Test Results Summary

Test Type Tool Result

---

UI Functional Testing Selenium + Pytest Passed
API Testing Postman + Newman Passed
Performance Testing JMeter Completed
Security Testing OWASP ZAP Completed
CI/CD Jenkins + Docker Passed
Automated Reporting JUnit + Allure Integrated

The automated UI and API tests execute successfully in the Jenkins
environment.

The JMeter execution produced an overall average response time of **159
ms** and an overall error rate of **0.11%**.

The OWASP ZAP scan generated a security report containing several
recommendations related to HTTP security headers, cookies, external
JavaScript resources, CSRF protection, and information disclosure.

---

# 13. Technologies Used

Technology Purpose

---

Python UI test implementation
Pytest Test execution framework
Selenium Browser automation
Postman API test design
Newman Automated Postman execution
Apache JMeter Performance testing
OWASP ZAP Security testing
Jenkins CI/CD automation
Docker Test/CI environment
Chromium Automated browser
ChromeDriver Selenium browser driver
Allure Test reporting
Git / GitHub Version control

---

# 14. Deliverables

The repository contains the main project deliverables:

### UI Tests

```text
ui-tests/
```

Contains Selenium/Pytest automation and Page Object Model classes.

### API Tests

```text
api-tests/postman/QAOps_Collection.postman_collection.json
```

Contains the Postman collection used for API validation.

### Performance Testing

```text
JMeter/
```

Contains JMeter evidence/screenshots.

### Security Testing

```text
security/
```

Contains the OWASP ZAP generated report.

### Test Plan

```text
docs/test-plan.md
```

Contains the test planning documentation.

### CI/CD

The Jenkins pipeline automates the UI and API test execution.

---

# 15. Conclusion

This project demonstrates the integration of several software quality
practices into a QAOps workflow.

The implemented solution covers:

- Functional browser automation with Selenium
- REST API testing with Postman and Newman
- Performance testing with Apache JMeter
- Security analysis with OWASP ZAP
- Continuous testing with Jenkins
- Containerized CI tooling with Docker
- Automated test reporting with JUnit and Allure

The final pipeline successfully executes the automated UI and API tests
and produces machine-readable test results suitable for CI/CD.

The performance tests showed an overall average response time of **159
ms** with an overall error rate of **0.11%** for the executed workload.

The security assessment identified multiple areas for improvement,
particularly security headers, cookie attributes, external JavaScript
integrity, CSRF protection, and information disclosure.

Overall, the project demonstrates how automated testing can be
integrated into a continuous quality workflow rather than being
performed only at the end of development.

---

# 16. Author

**Aymane Jemmaa**

Full Stack Developer\
Master's student in Computer Engineering & Artificial Intelligence

GitHub:\
https://github.com/aymanee04

Portfolio:\
https://aymanejemmaa.vercel.app/
