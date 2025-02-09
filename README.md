# GitHub to Lambda CI/CD Tool

A continuous integration and continuous deployment (CI/CD) tool that automatically updates AWS Lambda functions from GitHub repositories.

## Overview

This tool automates the process of deploying code changes from GitHub repositories to AWS Lambda functions. When changes are pushed to your GitHub repository, the tool automatically builds and deploys your updated code to the specified Lambda functions.

## Features

- Automated deployment from GitHub to AWS Lambda
- Supports multiple Lambda functions
- AWS CodeBuild integration for build process
- Secure handling of AWS credentials
- Configurable deployment settings

## Prerequisites

- AWS Account
- GitHub repository containing Lambda function code
- AWS IAM permissions for:
  - Lambda
  - CodeBuild
  - IAM roles
  - CloudWatch Logs

## Setup

1. Clone this repository
2. Configure AWS credentials
3. Update the buildspec.yml with your Lambda function details
4. Set up GitHub webhooks (if using) or configure GitHub Actions

## Configuration

### buildspec.yml

The buildspec.yml file contains the build and deployment specifications. Customize it according to your Lambda function requirements.

### Environment Variables

Set the following environment variables in your AWS CodeBuild project:

- `AWS_REGION`: Your AWS region
- `LAMBDA_FUNCTION_NAME`: Name of your target Lambda function
- Additional environment variables as needed

## Usage

1. Push your code changes to GitHub
2. The CI/CD pipeline will automatically:
   - Build your code
   - Run tests (if configured)
   - Deploy to Lambda

## Troubleshooting

Check CloudWatch Logs for build and deployment logs if you encounter any issues.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Add your license information here]

## Support

For issues and feature requests, please create a GitHub issue.
