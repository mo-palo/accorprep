# AI PDLC Tech Backbone

Accor Group  
May 28, 2026

---

## 1. Objective and Outcome

Accor's CD&T / Software Factory is preparing a large-scale AI-enabled PDLC transformation that will embed AI capabilities across all stages of the product development lifecycle for multiple delivery teams.

Before onboarding the first transformation teams (targeted September 2026), Accor would like to de-risk the technical foundation to avoid discovering integration, tooling, and operational blockers when teams are in flight.

### Context Objective

De-risk the technical foundation of Accor's AI-enabled PDLC by testing AI tool integrations end-to-end on a mock project within Accor's actual IT environment, so that the broader transformation can start with known constraints, identified blockers, and realistic expectations.

This is not a production-ready build. It is a technical exploration and de-risking engagement. Future efforts will adapt, adjust, and extend everything based on real project needs.

All configuration, validation, and evidence work is scoped to the agreed mock project and selected representative PDLC path. The engagement is not intended to cover, retrofit, or validate every Accor application, repository, team, or technical stack.

### Outcomes

- Surface integration blockers early
  - Discover what works, what doesn't, and what requires workarounds when AI tools (AccorGPT, Claude Code, Copilot) meet Accor's actual infrastructure (GitLab, Jira, ServiceNow, Splunk, Terraform, AWS).
- Test the full lifecycle at least once
  - Exercise every PDLC stage (requirements -> code -> test -> deploy -> monitor -> maintain) with AI augmentation to identify where gaps and friction points are, not to produce a polished result.
- Quantify what is realistic
  - Establish a baseline understanding of what AI can and cannot do today within Accor's constraints, so the transformation project sets achievable targets rather than aspirational ones.
- Document learnings, not just outputs
  - Capture what worked, what failed, what surprised, and what needs further investigation. This documentation is as valuable as technical configurations.
- Provide a starting point, not a final answer
  - First-pass configurations (prompts, agents, pipelines, quality gates) that give the transformation project something concrete to iterate on, knowing they will be significantly reworked on real projects.

By September 2026, Accor can confidently say:

- "We know where the real blockers are before they hit live teams"
- "We have a realistic picture of AI's current capabilities within our environment"
- "We have first-draft configurations that transformation teams can use as a starting point"
- "We know what needs more investment and what works well enough"
- "We can plan the transformation timeline with evidence, not assumptions"

---

## 2. Approach

The engagement is structured in three phases:

1. Initiation (unit S1): align, scope, prioritize (see scope and deliverables section for details)
2. Parallel execution: 2 technical streams + 1 functional stream
3. Wrap-up (unit S2): consolidate, document, hand over (see scope and deliverables section for details)

The technical streams deliver technical work units (see units Tx in the scope and deliverables section). The functional stream delivers functional work units (see units Fy in the scope and deliverables section). All elements produced by the streams are run using the mock project.

This structure maximizes value/cost ratio while keeping coordination manageable. The two technical streams share a Tech Lead who ensures consistency; the functional stream runs independently by the PO/PM who also provides overall project management.

### Technical Streams

Each technical stream performs technical work units. All technical work units have been sized for 2 weeks. They will be prioritized during initiation (S1) and can be reprioritized during steering committees.

- Team per stream: 2 Developers full-time, Tech Lead at 40%, PO/PM at 10%
- Cadence: each stream picks up the next prioritized technical work unit upon completing the previous one
- Scope: AI integration into coding, code review, testing, CI/CD pipelines, security, release/deploy, infrastructure provisioning, monitoring, maintenance, ITSM, documentation, and architecture/design

The Tech Lead bridges both streams to ensure shared patterns (prompts, agents, conventions) remain consistent and there are no conflicting configurations.

Initial technical scope identified: T4, T5, T7, T10, T11, and T12.

### Functional Stream

The functional stream performs functional units. The unit performed by this stream is identified in S1 (candidate: F2).

- Team: PO/PM at 80%, Tech Lead at 20%
- Cadence: picks up the next prioritized functional work unit upon completing the previous one
- Scope: AI augmentation of business requirements, product management, and project management workflows

Functional units run at a different pace: fewer hands-on activities and more stakeholder collaboration with Accor BAs, POs, and PMs. Tech Lead involvement ensures workflow designs remain technically feasible.

### Cross-Team Coordination and Governance

- Weekly sync (EM + TL + PO/PM): progress, blockers, dependency management
- Shared artifact repository: prompts, agents, and configurations are shared immediately across streams
- Prioritization adjustments: backlog can be re-sequenced if critical blockers emerge (agreed with Accor)
- Every 2 weeks steering committee: progress review, risk review, and mitigation decisions

### Additional Package

The project timeline can be extended to deliver additional work units before final wrap-up.

If Accor wants to proceed, they must notify PALO IT and initiate contractualization no later than Week 5. The additional package extends duration by 4 weeks and includes 4 technical units and 1 functional unit. Specific units are selected from the provided list during a steering committee before Week 6.

### Mock Project Requirements

The mock project is a multi-repo, AWS-deployed, GitFlow-managed application with enough infrastructure and operational surface to validate AI-augmented release orchestration, monitoring, security scanning, incident management, IaC authoring, and pipeline generation.

It must be realistic in structure but minimal in business logic: a tech backbone sandbox, not a product.

#### Key Architectural Characteristics

- Multi-repo: frontend, backend, and infra in separate GitLab repositories
- GitFlow branching: develop, release/*, hotfix/* branches aligned with Accor CD pipeline model
- Deployable to AWS (non-production dev and int environments)
- Produces telemetry: structured JSON logs, metrics, traces -> Splunk + CloudWatch
- Feature flags: 2-3 toggleable features for T4 feature-flipping validation
- Database with migrations: schema changes that trigger deployment validation

#### Suggested Functional Scenario

A simple "Team Directory" or "Internal Event Board" application:

- Frontend: list page, detail page, create form (3 routes, basic CRUD)
- Backend: REST API for entities (for example /api/events, /api/events/:id), auth middleware, health checks
- Database: 2 tables with simple relations and migration history
- Feature flags: toggle between list view/card view, and toggle a notifications feature

This provides enough surface for all work units without requiring domain complexity.

#### Minimum Complexity Thresholds

- Frontend: 5-8 components, 3 routes, 1 API service layer
- Backend: 5-6 endpoints, 2 domain entities, auth middleware, error handling, structured logging
- Terraform: 2 modules, 2 workspaces, 1 cross-stack data source
- Pipeline: 4 stages (build -> test -> scan -> deploy), 1 quality gate
- Dependencies: 15-20 direct dependencies per repo

#### Infrastructure Requirements (T11, T4)

- Terraform workspaces: 2 stacks
  - app-infra (compute, ALB, IAM)
  - data-infra (RDS, S3)
  - with cross-stack data sources
- AWS resources: ECS Fargate cluster, RDS PostgreSQL, ALB, S3 bucket, CloudWatch log groups, IAM roles
- CD pipeline: Accor-standard GitFlow Terraform pipeline in GitLab (deploy on merge to release/*)
- State management: remote state in S3 + DynamoDB lock table
- Environments: dev and int only (no production)

#### CI/CD Requirements (T12, T4)

- GitLab CI pipelines: .gitlab-ci.yml with build, test, scan, deploy stages
- SonarQube: quality gate configured (coverage, duplication thresholds)
- Artifact registry: container images pushed to GitLab Container Registry or ECR
- Pipeline variety: separate pipelines for frontend and backend (different build tools)

#### Observability Requirements (T5, T10)

- Application logging: structured JSON logs with correlation IDs -> Splunk
- CloudWatch: metrics and alarms for infrastructure signals (CPU, memory, 5xx count)
- Health endpoints: /health and /ready on backend
- Failure simulation: env var toggles to force errors (DB timeout, 5xx responses)
- SLO definitions: 2 SLOs, for example p99 latency < 500ms and error rate < 1%

#### Security Requirements (T7)

- Container images: Dockerfiles for frontend and backend (Trivy/Wiz scan targets)
- SAST surface: auth flow, input handling, SQL-adjacent queries for Checkmarx
- IaC policies: Terraform with security-relevant configs (security groups, IAM, encryption settings)
- Planted findings: 3-5 intentional security issues of varying severity for AI triage demo
- Dependency tree: realistic package manifests with some outdated dependencies

#### ITSM Integration Requirements (T10)

- Alert-to-incident path: monitoring alerts (T5) mappable to ServiceNow incident creation
- Deployment events: CD pipeline emits events consumable by ServiceNow change management
- CMDB: application components registered as configuration items
- Incident variety: failure simulation produces different incident types (infra, app, timeout)

---

## 3. Scope and Deliverables

### Technical Work Units

- T1: AI-Augmented Code Generation
- T2: AI-Augmented Code Review
- T3: AI-Augmented Testing & Quality
- T4: AI-Augmented Release & Deploy
- T5: AI-Augmented Monitoring & Alerting
- T6: AI-Augmented Maintenance & Bug Management
- T7: AI-Augmented Security & Compliance
- T8: AI-Augmented Code Documentation Generation
- T9: AI-Augmented Architecture & Technical Design
- T10: AI-Augmented ITSM & Incident Management
- T11: AI-Augmented Infrastructure Provisioning
- T12: AI-Augmented CI/CD Pipeline Generation & Quality Gates

### Functional Work Units

- F1: AI-Augmented Business Requirements Gathering
- F2: AI-Augmented Product Management
- F3: AI-Augmented Project Management

### S1: Initiation

Onboard team, align priorities, validate environment readiness, map existing PDLC stages and toolchain, and confirm sequencing/success criteria.

Must-have deliverables:

- Engagement plan with confirmed scope and prioritized backlog
- Prerequisites register (tool access, accounts, environments)
- PDLC stage mapping validated against Accor landscape documentation
- Risk-based prioritization of subsequent units
- Success criteria and measurable KPIs per unit
- Multi-repo complexity assessment: repositories, languages, dependencies, risk level for AI context coherence

Nice-to-have deliverables:

- Baseline measurements per KPI
- Preliminary gap analysis of AI integration points

Pre-requisites:

- PALO IT team accounts + tool access granted
- Named Accor counterparts available for daily collaboration
- Access to PDLC documentation and tool landscape
- Accor leadership available for prioritization workshop

Exclusions:

- No forked mock project required for this unit
- No hands-on technical implementation
- No tool configuration or code changes
- Unit cannot be delivered if Accor counterparts are unavailable during the week

Resources: 1 Product Owner, 1 Tech Lead, 4 Developers (full-time)  
Duration: 1 week

### T1: AI-Augmented Code Generation

Define and operationalize AI-assisted coding workflow using Accor toolchain (AccorGPT/Claude Code, Microsoft Copilot, JetBrains/VSCode). Create standards, prompt libraries, agents, and validate multi-repo context coherence.

Must-have deliverables:

- Documented AI-assisted coding workflow
- Coding standards/conventions enforced through AI prompts/context files
- Prompt library for common Accor patterns (CRUD, API integration, error handling)
- Multi-repo context validation across repositories scoped in S1

Nice-to-have deliverables:

- Custom agent definitions for Accor architectural patterns
- Developer experience survey (friction, trust, quality perception)

Pre-requisites:

- S1 completed
- Forked mock project available (SPA + backend + DB, multi-repo)
- AccorGPT access and Claude Code configured
- Accor coding standards documentation
- Accor engineering lead available (minimum 2 days/week)

Exclusions:

- Code review automation (T2)
- Test generation (T3)
- Tool selection (already selected)
- Production deployment
- Defining standards without Accor input

Resources: PO 10%, TL 40%, 2 Developers full-time  
Duration: 2 weeks

### T2: AI-Augmented Code Review

Set up AI-assisted code review in GitLab with automated suggestions, quality gates, and standards enforcement.

Must-have deliverables:

- AI-powered code review integrated in GitLab MR workflow
- Quality gates for coding standards (linting, conventions)
- Configuration documentation for review agents

Nice-to-have deliverables:

- Auto-fix suggestions for common issues
- SonarQube integration for AI-reviewed quality thresholds

Pre-requisites:

- T1 completed
- Forked mock project available
- GitLab CI/CD admin access
- SonarQube access
- Accor DevOps engineer available (minimum 2 days/week)

Exclusions:

- Code generation (T1)
- Security-specific scanning (T7)
- Manual review process redesign
- Unilateral quality gate decisions (must be validated with Accor engineering)

Resources: PO 10%, TL 40%, 2 Developers full-time  
Duration: 2 weeks

### T3: AI-Augmented Testing & Quality

Embed AI into test stage: automated test generation (unit/integration/E2E), coverage analysis, gap detection, and CI triggers.

Must-have deliverables:

- AI-generated unit tests for frontend and backend
- CI integration (test generation triggered on merge request)
- Coverage analysis and gap report

Nice-to-have deliverables:

- AI-generated E2E tests (Playwright)
- AI-assisted test maintenance
- BrowserStack/XRay integration evaluation

Pre-requisites:

- S1 completed
- Forked mock project available
- GitLab CI access
- Playwright / SonarQube / XRay access
- Accor QA lead available (minimum 1 day/week)

Exclusions:

- Performance/load testing
- Manual QA process redesign
- Test environment provisioning
- Final strategy cannot be set without Accor QA validation

Resources: PO 10%, TL 40%, 2 Developers full-time  
Duration: 2 weeks

### T4: AI-Augmented Release & Deploy

Embed AI into release/deployment orchestration using Accor RBAC/CD Terraform pipeline (GitFlow-based), feature flag orchestration, and rollback support.

Must-have deliverables:

- AI-assisted deployment configurations integrated with Accor Terraform CD pipeline
- AI-driven release workflow (pre-deploy checks, approval recommendations, go/no-go signals)
- AI-assisted rollback decision automation
- Feature-flipping enablement and validation across environments
- Release notes generation from deployment diff

Nice-to-have deliverables:

- CMDB (ServiceNow) integration for change requests and release tracking
- Canary/blue-green recommendations
- Deployment history analysis for failure patterns
- Multi-environment promotion workflow with AI validation

Pre-requisites:

- S1 completed
- Forked mock project available
- Access to Accor Terraform CD pipeline with deployment permissions
- AWS non-production access
- Feature flag tool access
- Accor Platform Engineering available (minimum 3 days/week)

Exclusions:

- Production deployment
- Terraform module authoring/IaC generation (T11)
- CI/CD pipeline creation/quality gate definition (T12)
- Landing zone design/modification
- Network/VPN infrastructure changes
- Migration to FluxCD/ArgoCD

Resources: PO 10%, TL 40%, 2 Developers full-time  
Duration: 2 weeks

### T5: AI-Augmented Monitoring & Alerting

Embed AI into detection/alerting: anomaly detection, context enrichment, noise reduction, and SLO-based thresholds.

Must-have deliverables:

- AI-augmented anomaly detection and incident identification (Splunk + CloudWatch)
- Automated alert enrichment with deployment/commit context
- Alert noise reduction via filtering/correlation
- SLO-based alerting when error budgets are at risk

Nice-to-have deliverables:

- Zabbix/ITOM correlation
- Slack webhook integration for AI-enriched notifications
- Predictive alerting from leading indicators

Pre-requisites:

- S1 completed
- Forked mock project deployed
- Splunk/O11Y + CloudWatch write access for alert config
- Monitoring dashboard access
- Accor Ops/SRE available (minimum 3 days/week)

Exclusions:

- Bug triage/fix workflows (T6)
- ServiceNow integration (T10)
- Security event monitoring (T7)
- Alert config without Accor Ops validation

Resources: PO 10%, TL 40%, 2 Developers full-time  
Duration: 2 weeks

### T6: AI-Augmented Maintenance & Bug Management

Embed AI in bug lifecycle and maintenance workflow: triage, repro info requests, root cause identification, and fix suggestions.

Must-have deliverables:

- AI-powered Jira bug triage (priority/classification/labeling)
- Automated requests for missing repro info
- Code-level root cause identification from bug descriptions + recent changes
- AI-suggested fixes for simple/recurring patterns (human-reviewed)

Nice-to-have deliverables:

- Recurring bug pattern detection
- Toil identification and automation recommendations
- Technical debt prioritization based on bug frequency/impact

Pre-requisites:

- S1 completed
- T5 completed
- Forked mock project deployed
- Jira automation permissions
- Accor dev team availability (minimum 2 days/week)
- Historical bug data access

Exclusions:

- Monitoring/alerting setup (T5)
- ServiceNow incident/change/problem mgmt (T10)
- Security incident response (T7)
- On-call process redesign
- Triage rules without Accor sign-off

Resources: PO 10%, TL 40%, 2 Developers full-time  
Duration: 2 weeks

### T7: AI-Augmented Security & Compliance

Embed AI in PDLC security checks: scan interpretation, vulnerability-to-fix suggestions, compliance docs, policy-as-code validation.

Must-have deliverables:

- AI-assisted scan interpretation (Checkmarx, Trivy, Wiz) with prioritized remediation
- Automated vulnerability-to-fix suggestions in merge requests
- Security findings report with AI-recommended remediations
- Policy-as-code validation against security rules

Nice-to-have deliverables:

- AI-generated compliance documentation
- DefectDojo integration
- Imperva WAF event correlation

Pre-requisites:

- S1 completed
- Forked mock project available
- Checkmarx/Trivy/Wiz access
- Accor Cybersecurity engagement (minimum 3 days/week)
- Existing security/compliance policies documented and accessible

Exclusions:

- Penetration testing
- Security architecture redesign
- Vault secrets management setup
- Compliance certification activities
- Unit postponed/descoped if Cybersecurity team unavailable

Resources: PO 10%, TL 40%, 2 Developers full-time  
Duration: 2 weeks

### T8: AI-Augmented Code Documentation Generation

Embed AI in documentation workflows: technical docs from code, APIs, ADRs, and freshness checks.

Must-have deliverables:

- AI-generated technical documentation from codebase (architecture, APIs, modules)
- AI-generated ADRs from code changes and design decisions
- Confluence integration for publishing
- Documentation freshness validation (stale doc detection)

Nice-to-have deliverables:

- AI-generated onboarding docs
- Automated changelog generation from merge requests
- Diagram generation (architecture/sequence/flow)
- Documentation quality gates in CI

Pre-requisites:

- S1 completed
- Forked mock project available
- Confluence publishing access
- Existing Accor documentation standards/templates
- Accor documentation owner available (minimum 1 day/week)

Exclusions:

- User-facing product documentation
- Training material creation
- Knowledge transfer sessions (covered in S2)
- Template creation without Accor standards review

Resources: PO 10%, TL 40%, 2 Developers full-time  
Duration: 2 weeks

### T9: AI-Augmented Architecture & Technical Design

Embed AI in design-time architecture workflows: solution design, impact analysis, pattern recommendations, decision support.

Must-have deliverables:

- AI-assisted solution design workflow
- AI-powered impact analysis across repositories
- Design pattern recommendations aligned to Accor conventions/constraints
- Architecture decision support (precedents, trade-offs, risks)

Nice-to-have deliverables:

- Technical debt identification/classification through architecture analysis
- LeanIX or CMDB integration for architecture registry updates
- AI-assisted technology choice evaluation
- Design review automation before human review

Pre-requisites:

- S1 completed
- Forked mock project available
- Confluence and/or Notion access
- Existing architecture standards/conventions from Accor
- Accor Solution Architect or Tech Lead available (minimum 2 days/week)

Exclusions:

- Redesign of Accor production architecture
- Enterprise architecture governance changes
- LeanIX landscape-level modeling
- Unit postponed/descoped if architecture counterpart unavailable

Resources: PO 10%, TL 40%, 2 Developers full-time  
Duration: 2 weeks

### T10: AI-Augmented ITSM & Incident Management

Embed AI in ITSM/incident flow: incident creation from alerts, triage/routing, change request generation, and CMDB context enrichment via ServiceNow.

Must-have deliverables:

- AI-assisted incident creation (Splunk/CloudWatch -> ServiceNow)
- Automated incident triage (severity, category, routing)
- AI-generated change requests from resolved incidents
- Knowledge base article generation from resolved incidents for coding-agent ingestion

Nice-to-have deliverables:

- Root-cause correlation into problem records
- CMDB enrichment suggestions from incidents/deployments
- Automated post-incident review generation
- Predictive incident detection from log/metric trends

Pre-requisites:

- S1 completed
- Forked mock project available
- ServiceNow access (incident/change/problem/CMDB)
- T5 completed or in progress
- Accor ITSM/ServiceNow team engagement (minimum 2 days/week)
- Existing incident categorization/routing rules documented

Exclusions:

- ServiceNow platform customization/development
- ITSM process redesign/governance changes
- CMDB data quality remediation
- Non-ServiceNow ITSM integrations
- Unit postponed/descoped if ServiceNow team unavailable

Resources: PO 10%, TL 40%, 2 Developers full-time  
Duration: 2 weeks

### T11: AI-Augmented Infrastructure Provisioning

Embed AI in IaC authoring/validation: module generation, dependency analysis, refactoring, apply troubleshooting, shift-left compliance.

Must-have deliverables:

- AI-assisted Terraform module generation from requirements/architecture intent
- AI-powered IaC review against Accor conventions, security policies, naming standards
- Cross-stack dependency analysis before merge
- Terraform apply troubleshooting (dependency cycles, provider conflicts, state lock issues)

Nice-to-have deliverables:

- IaC refactoring recommendations (duplicate pattern extraction)
- Shift-left cost awareness at authoring time
- State surgery assistance (imports/moves/removals) with safety checks
- AI-generated infrastructure documentation from Terraform/state
- Migration assistance for deprecated Terraform patterns

Pre-requisites:

- S1 completed
- Forked mock project available
- AWS dev/int access with Terraform state visibility
- Existing Terraform modules/conventions from Accor
- Accor Platform Engineering/CloudOps engagement (minimum 2 days/week)

Exclusions:

- Production infrastructure changes
- AWS account/org setup
- FinOps tool implementation/configuration
- Network architecture or security group redesign
- Drift detection (handled natively by Terraform plan)
- Unit postponed/descoped if Platform Engineering unavailable

Resources: PO 10%, TL 40%, 2 Developers full-time  
Duration: 2 weeks

### T12: AI-Augmented Pipeline Generation & Quality Gates

Embed AI in CI/CD pipeline-as-code lifecycle: generation, quality gate definition, optimization, failure diagnosis, and drift detection.

Must-have deliverables:

- AI-assisted pipeline generation from project structure
- AI-defined quality gates based on codebase analysis
- Pipeline failure diagnosis from logs with root cause and fixes
- Pipeline optimization (slow stage/redundancy/cache opportunities)
- Pipeline drift detection versus Accor standards

Nice-to-have deliverables:

- Pipeline template library for common Accor project types (Java, Node.js, Python)
- Quality gate evolution over time based on maturity/historical trends
- Cross-pipeline dependency analysis across repositories

Pre-requisites:

- S1 completed
- Forked mock project available
- GitLab CI/CD editing access
- SonarQube access
- Existing pipeline templates/standards from Accor
- Accor DevOps/CI-CD team available (minimum 2 days/week)

Exclusions:

- GitLab platform administration/runner management
- SonarQube server configuration/rule customization
- Production pipeline execution
- Build tool migration
- Unit postponed/descoped if DevOps team unavailable

Resources: PO 10%, TL 40%, 2 Developers full-time  
Duration: 2 weeks

### F1: AI-Augmented Business Requirements Gathering

Embed AI in requirements elicitation: extraction, structuring, traceability, and change impact analysis.

Must-have deliverables:

- AI-assisted requirements extraction from transcripts/documents
- Structured requirements repository with AI-generated traceability matrix
- AI-powered impact analysis for requirement changes
- Requirements quality validation (completeness/consistency/testability)

Nice-to-have deliverables:

- AI-generated acceptance criteria
- AI-generated stakeholder communication summaries/meeting minutes
- Requirements-to-code traceability proof of concept

Pre-requisites:

- S1 completed
- Forked mock project available
- Jira/Confluence access
- Sample requirements documentation from Accor
- Accor BA or PO engagement (minimum 3 days/week)

Exclusions:

- Real-project requirements gathering
- Business/domain expertise provision
- Product strategy/roadmap definition (F2)
- No delivery without Accor BA involvement

Resources: PO 80%, TL 20%  
Duration: 4 weeks

### F2: AI-Augmented Product Management

Embed AI in product management workflows: story generation, backlog prioritization, estimation, criteria generation, analytics interpretation.

Must-have deliverables:

- AI-assisted epic/story generation in Jira from product requirements
- AI-generated acceptance criteria and test scenarios from stories
- AI-powered effort estimation from codebase complexity analysis
- AI-assisted backlog prioritization recommendations

Nice-to-have deliverables:

- AI-assisted roadmap scenario modeling
- Product analytics interpretation and insight generation
- Automated dependency mapping across epics/features

Pre-requisites:

- S1 completed
- Forked mock project available
- Jira/Confluence access
- Sample product backlog from Accor
- Accor Product Owner engagement (minimum 3 days/week)

Exclusions:

- Project management workflows (F3)
- Business requirements elicitation (F1)
- Product strategy definition or real product decisions
- No delivery without Accor PO involvement

Resources: PO 80%, TL 20%  
Duration: 4 weeks

### F3: AI-Augmented Project Management

Embed AI in project management workflows: sprint planning, forecasting, risk identification, status reporting automation, resource optimization.

Must-have deliverables:

- AI-assisted sprint planning (story selection, capacity recommendations)
- Automated status report generation from Jira data
- AI-powered risk identification and early warnings
- Velocity forecasting and delivery date prediction

Nice-to-have deliverables:

- AI-generated stakeholder communication drafts
- Resource allocation optimization suggestions
- Retrospective insight extraction and action tracking

Pre-requisites:

- S1 completed
- Forked mock project available
- Jira/Confluence/MS Teams access
- Historical project delivery data from Accor
- Accor Delivery/Project Manager engagement (minimum 3 days/week)

Exclusions:

- Product management workflows (F2)
- Actual project delivery/team management
- PMO process redesign/organizational change
- No delivery without Accor PM involvement

Resources: PO 80%, TL 20%  
Duration: 4 weeks

### S2: Wrap-Up

Co-run the mock project for one full sprint using all AI-augmented PDLC tools from previous units. Validate end-to-end flow, measure cycle-time indications, and produce final handover.

Must-have deliverables:

- Full sprint execution with AI-augmented PDLC (requirements -> code -> test -> deploy -> operate)
- Indicative end-to-end cycle timing / qualitative improvement evidence where baseline exists
- Execution report: findings, metrics, what worked, what did not
- Final handover package (configurations, prompts, agents, quality gates)
- Recommendations for full-scale rollout (input to transformation phase 2)

Nice-to-have deliverables:

- Knowledge transfer sessions with Accor teams
- Workflow video recordings for training
- Maturity assessment per PDLC stage with improvement roadmap

Pre-requisites:

- All units completed or explicitly descoped
- Forked mock project fully set up with integrations
- Full Accor cross-functional team availability during 2-week sprint
- Accor leadership available for sprint review and final report validation

Exclusions:

- New feature development/tool exploration
- Organizational change management
- Contract negotiations for phase 2
- Sprint cannot run without Accor participation

Resources: 1 Product Owner, 1 Tech Lead, 4 Developers (all full-time)  
Duration: 2 weeks

---

## 4. Timeline

### Base Timeline

6 technical units and 1 functional unit in 9 weeks.

(Visual plan indicates S1 in week 1, parallel Tx/Fy execution across subsequent weeks, and S2 in final phase.)

### Timeline with Additional Package (Orange)

10 technical units and 2 functional units in 13 weeks.

(Visual plan extends parallel Tx/Fy execution and shifts S2 to later weeks.)

---

## 5. Team Composition

### Team Setup

- Engagement Manager
- AI Product Owner
- AI Lead
- AI Engineer
- AI Engineer
- AI Engineer
- AI Engineer

### Role Definitions

#### AI Lead

Responsibilities:

- Technical coordination across streams (technical and functional)
- Architecture decisions for AI integration patterns
- Ensure consistency/coherence across work units (shared prompts, agents, standards)
- Review/validate technical deliverables
- Interface with Accor engineering leadership
- Participate in functional units (20%) for feasibility and support

Key interactions:

- Engineering Lead
- Architect

#### AI Engineer

Responsibilities:

- Hands-on implementation of technical work units
- Configure AI tooling, prompts, agents, pipelines
- Validate AI outputs against Accor standards
- Document configurations and implementation patterns
- Participate in S1 and S2 at full capacity

Key interactions:

- Developers
- Platform Engineers
- QA leads
- Ops/SRE team

#### AI Product Owner

Responsibilities:

- Project management (20%): sprint planning, progress tracking, reporting, dependencies
- Functional unit execution (80%): lead F units and validate AI-augmented workflows with Accor stakeholders

Key interactions:

- Business Analysts
- Product Owners
- Project Managers
- Delivery Leads

#### Engagement Manager

Responsibilities:

- Overall engagement governance
- Risk management and escalation
- Customer relationship management with Accor leadership
- Monthly steering facilitation
- Commercial and contractual oversight
- Ensure alignment between PALO IT delivery and Accor expectations

Key interactions:

- Leadership

---

## 6. Pre-Requisites, Assumptions, Risks, and Exclusions

### Pre-Requisites (Before End of S1)

- Mock project forked, sanitized, and available in GitLab
- Isolated environments provisioned (dev/int minimum)
- PALO IT team accounts created (GitLab, Jira, Confluence, AWS, ServiceNow, Splunk)
- AI tool licenses allocated to PALO IT team members
- Existing PDLC documentation and standards accessible (Confluence/Notion/SharePoint)
- Network/VPN access for PALO IT team (if remote)

### Assumptions

- PALO IT delivers from Thailand unless otherwise confirmed
- Accor provides forked, sanitized mock project (SPA frontend + lightweight backend + DB) before T0
- Mock project is multi-repo and representative of Accor delivery pattern
- Accor provides isolated environments (dev/int/prod or equivalent) without production data exposure
- All tool access (GitLab, Jira, Confluence, ServiceNow, Splunk, AWS, Terraform, etc.) is granted in first week (S1)
- Mock project business logic remains simple; complexity is in PDLC flow
- Named Accor counterparts are committed for engagement duration
- Accor counterparts are available at specified frequency per work unit
- Accor leadership is available for S1 prioritization workshop and S2 final presentation
- Accor provides existing standards/conventions/documentation for each PDLC stage
- AI tools are already selected by Accor (AccorGPT/Claude Code and Microsoft Copilot)
- AccorGPT (LiteLLM + Bedrock) is operational and accessible from day one
- AI model capabilities are current-generation (e.g., Claude Opus/Sonnet 4.6, GPT-5.4+), no custom fine-tuning required
- Data residency and AI governance are handled by Accor approved endpoints
- AI licenses are provided by Accor for PALO IT team
- Nice-to-have deliverables are best-effort and not contractually committed
- Outputs are starting points for transformation, not production-ready configurations
- No production deployment or production data access required
- Engagement excludes org change management, training rollout, or team onboarding beyond S2 knowledge transfer

### Risks

- Accor counterpart unavailability (high)
  - Mitigation: prerequisite explicit per unit; units paused/deprioritized if counterparts unavailable
- ServiceNow integration complexity and access delays for T10 (high)
  - Mitigation: scope must-haves to incident creation + triage; deprioritize if access delayed
- Late T0 start shrinking timeline window (medium)
  - Mitigation: adjust unit count; prioritize highest-risk units first
- Security team engagement constraints for T7 (high)
  - Mitigation: reduce must-haves to scan interpretation + fix suggestions; move policy-as-code to nice-to-have; postpone if needed
- Multi-repo AI context limitations in T1 (medium)
  - Mitigation: treat as validation; document limitations/workarounds instead of forcing full solution
- Mock project too simple (medium)
  - Mitigation: assess complexity in S1 and adjust scope; multi-repo remains prerequisite
- Tool access delays (medium)
  - Mitigation: submit requests before T0; validate access in S1 gate; resequence blocked units
- AI tool evolution during engagement (medium)
  - Mitigation: document and version-pin tool/config versions; reevaluate in transformation phase
- Cross-stream dependency blocks (low)
  - Mitigation: sequence dependent units in same stream; prioritize independent units in parallel stream
- Terraform state not accessible for T11 (medium)
  - Mitigation: if restricted, work on fresh Terraform from scratch on mock project
- Accor standards undocumented (low)
  - Mitigation: capture what exists in S1; propose draft for validation if undocumented
- KPI definition difficulty on mock project (low)
  - Mitigation: define measurable indicators in S1; use qualitative metrics where needed

### Risk Acceptance

By nature, this is a de-risking engagement. Some work units may conclude that capabilities do not yet work well enough or require more investment than anticipated. These are valid outcomes and part of success criteria.

A unit that identifies and documents a blocker clearly is as successful as a unit producing a working configuration.

### Exclusions

- Production deployment or production data access
- Tool selection or vendor evaluation
- Custom AI model training or fine-tuning
- Organizational transformation/team restructuring/process redesign
- Full-scale rollout to Accor delivery teams (post-engagement)
- Integration with every tool in Accor landscape (limited to S1-confirmed scope)
- Performance/load testing, penetration testing, compliance certification
- Third-party tool procurement/licensing/subscription management
- Delivery of any unit without active Accor counterpart involvement
- Guaranteed productivity gains (engagement is exploratory)

---

## Contact

Frederic BERNAROYAT  
fbernaroyat@palo-it.com  
+66 805144156
