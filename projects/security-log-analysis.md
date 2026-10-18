# Security Log Analysis

## Project Overview
This beginner cybersecurity project focuses on analysing sample authentication logs to identify potentially suspicious login activity.

## Objective
Practise reviewing login records, identifying unusual patterns, and recommending defensive security measures.

## Tools Used
- GitHub for project documentation
- Sample authentication logs (to be added)
- Basic log analysis techniques

## Methodology
1. Review sample authentication records.
2. Identify failed and successful login attempts.
3. Look for repeated failed logins and unusual activity.
4. Record suspicious patterns for further investigation.
5. Recommend appropriate defensive actions.

## Findings
The sample authentication logs were reviewed to identify repeated failed login attempts and successful logins following those failures.

Observation 1: Repeated failed logins

Username: thabo

Source IP: 192.0.2.11

Failed attempts: 4

Time range: 08:05:30–08:06:08 on 15 October 2026

Subsequent event: Successful login at 08:06:21.

Observation 2: Successful login after repeated failures

The account thabo recorded four consecutive failed login attempts followed by a successful login 13 seconds after the final failure.

This pattern may indicate repeated password guessing or another authentication issue. Further investigation would be required before determining whether the activity was malicious.

Observation 3: Repeated failures on the admin account

Username: admin

Source IP: 192.0.2.12

Failed attempts: 3

Time range: 08:10:02–08:10:29 on 15 October 2026

The three consecutive failures warrant review, although no successful login from this source IP is shown immediately afterward in the supplied sample.

Recommendations

Review authentication logs for additional activity involving the affected accounts and source IPs.

Check whether the successful login was expected and authorised.

Apply appropriate account lockout or rate-limiting controls.

Enable multi-factor authentication where supported.

Continue monitoring for repeated failures and unusual login patterns.

Limitations

This analysis uses a small sample dataset created for training. The observations do not establish that an account was compromised or that an attack occurred.

## Recommendations
- Monitor repeated failed login attempts.
- Investigate unusual login activity.
- Use strong passwords and multi-factor authentication.
- Follow incident reporting procedures.

## Learning Outcomes
- Understanding authentication logs
- Recognising potentially suspicious login patterns
- Practising security monitoring and documentation

## Project Status
Documentation created. Practical analysis and evidence still need to be added.

## Disclaimer
This is a learning project using sample data. No real organisation's systems were accessed.

## Skills Demonstrated

- Authentication log analysis
- Identification of repeated failed login attempts
- Recognition of potentially suspicious login patterns
- Basic security investigation and evidence-based reporting
- Defensive security recommendations
- GitHub documentation and version control
