## Overview
Production-grade multi-tenant SaaS backend built with FastAPI.

## Goals
- Multi-tenancy
- RBAC
- Subscription billing
- Async performance

## Architecture (Draft)
FastAPI → Domain Services → Async DB → Redis → Workers
