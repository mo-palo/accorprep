# AI PDLC Tech Backbone

Accor Group  
May 28, 2026

---

## 1. Objective and Outcome

Accor's CD&T / Software Factory is preparing a large-scale AI-enabled PDLC transformation that will embed AI capabilities across all stages of the product development lifecycle for multiple delivery teams.

Before onboarding the first transformation teams (targeted September 2026), Accor would like to de-risk the technical foundation to avoid discovering integration, tooling, and operational blockers when teams are in flight.

Objective:

De-risk the technical foundation of Accor's AI-enabled PDLC by testing AI tool integrations end-to-end on a mock project within Accor's actual IT environment, so the broader transformation can start with known constraints, identified blockers, and realistic expectations.

This is not a production-ready build. It is a technical exploration and de-risking engagement. Future efforts will adapt, adjust, and extend everything based on real project needs.

All configuration, validation, and evidence work is scoped to the agreed mock project and selected representative PDLC path. The engagement is not intended to cover, retrofit, or validate every Accor application, repository, team, or technical stack.

### Outcomes

- Surface integration blockers early:
  - Discover what works, what does not, and what requires workarounds when AI tools (AccorGPT, Claude Code, Copilot) meet Accor's infrastructure (GitLab, Jira, ServiceNow, Splunk, Terraform, AWS).
- Test the full lifecycle at least once:
  - Exercise every PDLC stage (requirements -> code -> test -> deploy -> monitor -> maintain) with AI augmentation to identify gaps and friction points.
- Quantify what is realistic:
  - Establish a baseline understanding of what AI can and cannot do today within Accor constraints.
- Document learnings, not just outputs:
  - Capture what worked, what failed, what surprised, and what needs further investigation.
- Provide a starting point, not a final answer:
  - Deliver first-pass configurations (prompts, agents, pipelines, quality gates) as a baseline for future iteration.

By September 2026, Accor can confidently say:

- "We know where the real blockers are - before they hit live teams"
- "We have a realistic picture of AI's current capabilities within our environment"
- "We have first-draft configurations that transformation teams can use as a starting point"
- "We know what needs more investment and what works well enough"
- "We can plan the transformation timeline with evidence, not assumptions"

---

## 2. Approach

The engagement is structured in three phases:

1. Initiation (unit S1) - align, scope, prioritize.
2. Parallel execution - 2 technical streams + 1 functional stream.
3. Wrap-up (unit S2) - consolidate, document, hand over.

The technical streams deliver technical work units (Tx in the scope and deliverables section).
The functional stream delivers functional work units (Fy in the scope and deliverables section).
All produced elements are run using the mock project.

This structure maximizes value/cost while keeping coordination manageable.
The two technical streams share a Tech Lead for consistency.
The functional stream runs independently through the PO/PM, who also provides overall project management.

### Technical streams

Each technical stream performs technical work units (sized for 2 weeks).
Units are prioritized during S1 and can be reprioritized at steering committees.

- Team per stream: 2 Developers full-time, Tech Lead at 40%, PO/PM at 10%.
- Cadence: each stream picks up the next prioritized technical unit after completing the previous one.
- Scope: AI integration into coding, code review, testing, CI/CD, security, release/deploy, infrastructure provisioning, monitoring, maintenance, ITSM, documentation, and architecture/design.

The Tech Lead bridges both streams so shared patterns (prompts, agents, conventions) remain consistent and non-conflicting.

Initial technical scope candidates: T4, T5, T7, T10, T11, T12.

### Functional stream

The functional stream performs functional units (identified in S1; candidate is F2).

- Team: PO/PM at 80%, Tech Lead at 20%.
- Cadence: picks up the next prioritized functional unit after completing the previous one.
- Scope: AI augmentation of business requirements, product management, and project management workflows.

Functional units run at a different pace (less hands-on, more stakeholder collaboration).
Tech Lead participation ensures technical feasibility and possible implementation support.

### Cross-team coordination and governance

- Weekly sync (EM + TL + PO/PM): progress, blockers, dependencies.
- Shared artifact repository: prompts, agents, and configs shared across streams.
- Prioritization adjustments: backlog may be resequenced if critical blockers emerge (with Accor agreement).
- Steering committee every 2 weeks: progress review, risk review, mitigation decisions.

### Additional package

The timeline can be extended for additional units before final wrap-up.

If Accor proceeds, notification and contractualization are required by Week 5.
The additional package extends the project by 4 weeks and includes 4 technical units and 1 functional unit, selected in a steering committee before Week 6.

### Mock project requirements

The mock project is a multi-repo, AWS-deployed, GitFlow-managed application with enough infrastructure and operational surface to validate AI-augmented release orchestration, monitoring, security scanning, incident management, IaC authoring, and pipeline generation.

It must be realistic in structure but minimal in business logic (a tech backbone sandbox, not a product).

Key architectural characteristics:

- Multi-repo: frontend, backend, and infra in separate GitLab repos.
- GitFlow branching: develop, release/*, hotfix/* branches.
- Deployable to AWS (non-production dev and int environments).
- Telemetry output: structured JSON logs, metrics, traces -> Splunk + CloudWatch.
- Feature flags: 2-3 toggleable features for T4 validation.
- Database with migrations: schema changes trigger deployment validation.

### Mock project suggested scenario

A simple "Team Directory" or "Internal Event Board" app:

- Frontend: list page, detail page, create form (3 routes, basic CRUD).
- Backend: REST API (for example, /api/events, /api/events/:id), auth middleware, health checks.
- Database: 2 tables with simple relations and migration history.
- Feature flags: toggle list/card view and a notifications feature.

### Minimum complexity thresholds

- Frontend: 5-8 components, 3 routes, 1 API service layer.
- Backend: 5-6 endpoints, 2 domain entities, auth middleware, error handling, structured logging.
- Terraform: 2 modules, 2 workspaces, 1 cross-stack data source.
- Pipeline: 4 stages (build -> test -> scan -> deploy), 1 quality gate.
- Dependencies: 15-20 direct dependencies per repo.

### Infrastructure requirements (T11, T4)

- Terraform workspaces: 2 stacks:
  - app-infra (compute, ALB, IAM)
  - data-infra (RDS, S3)
  - with cross-stack data sources
- AWS resources: ECS Fargate cluster, RDS PostgreSQL, ALB, S3 bucket, CloudWatch log groups, IAM roles.
- CD pipeline: Accor-standard GitFlow Terraform pipeline in GitLab (deploy on merge to release/*).
- State management: remote state in S3 + DynamoDB lock table.
- Environments: dev and int only (no production).

### CI/CD requirements (T12, T4)

- GitLab CI pipelines: .gitlab-ci.yml with build, test, scan, deploy stages.
- SonarQube quality gate configured (coverage, duplication thresholds).
- Artifact registry: container images pushed to GitLab Container Registry or ECR.
- Pipeline variety: separate frontend and backend pipelines (different build tools).

### Observability requirements (T5, T10)

- Application logging: structured JSON logs with correlation IDs -> Splunk.
- CloudWatch: metrics and alarms for infrastructure signals (CPU, memory, 5xx count).
- Health endpoints: /health and /ready on backend.
- Failure simulation: env var toggles to force errors (DB timeout, 5xx responses).
- SLO definitions: 2 SLOs, for example:
  - p99 latency < 500ms
  - error rate < 1%

### Security requirements (T7)

- Container images: Dockerfiles for frontend/backend (Trivy/Wiz scan targets).
- SAST surface: auth flow, input handling, SQL-adjacent queries for Checkmarx.
- IaC policies: Terraform with security-relevant configs (security groups, IAM, encryption).
- Planted findings: 3-5 intentional security issues of varying severity.
- Dependency tree: realistic package manifests with some outdated dependencies.

### ITSM integration requirements (T10)

- Alert-to-incident path: monitoring alerts (T5) mappable to ServiceNow incident creation.
- Deployment events: CD pipeline emits events for ServiceNow change management.
- CMDB: app components registered as CIs.
- Incident variety: failure simulation covers infra, app, timeout incident types.

---

## 3. Scope and Deliverables

### Technical work units

- T1: AI-Augmented Code Generation
- T2: AI-Augmented Code Review
- T3: AI-Augmented Testing and Quality
- T4: AI-Augmented Release and Deploy
- T5: AI-Augmented Monitoring and Alerting
- T6: AI-Augmented Maintenance and Bug Management
- T7: AI-Augmented Security and Compliance
- T8: AI-Augmented Code Documentation Generation
- T9: AI-Augmented Architecture and Technical Design
- T10: AI-Augmented ITSM and Incident Management
- T11: AI-Augmented Infrastructure Provisioning
- T12: AI-Augmented CI/CD Pipeline Generation and Quality Gates

### Functional work units

- F1: AI-Augmented Business Requirements Gathering
- F2: AI-Augmented Product Management
- F3: AI-Augmented Project Management

### S1: Initiation

Purpose:
Onboard team, align priorities, validate environment readiness, map PDLC and toolchain, confirm sequencing and success criteria.

Must-have deliverables:

- Engagement plan with confirmed scope and prioritized backlog.
- Prerequisites register (tool access, accounts, environments).
- PDLC stage mapping validated against Accor documentation.
- Risk-based prioritization of subsequent units.
- Success criteria and measurable KPIs per work unit.
- Multi-repo complexity assessment (repos, languages, dependencies, AI context coherence risk).

Nice-to-have deliverables:

- Baseline KPI measurements before AI augmentation.
- Preliminary gap analysis of AI integration points.

Pre-requisites:

- PALO IT accounts and tool access granted.
- Named Accor counterparts available daily.
- Access to PDLC documentation and tool landscape.
- Leadership available for prioritization workshop.

Exclusions:

- No forked mock project required for this unit.
- No hands-on technical implementation.
- No tool configuration or code changes.
- Cannot deliver if Accor counterparts are unavailable during this week.

Resources: 1 Product Owner, 1 Tech Lead, 4 Developers (full-time).  
Duration: 1 week.

### T1: AI-Augmented Code Generation

Purpose:
Define and operationalize AI-assisted coding workflow (AccorGPT/Claude Code, Copilot, JetBrains/VSCode), standards, prompts, and multi-repo context coherence.

Must-have deliverables:

- Documented AI-assisted coding workflow.
- Coding standards and conventions enforced via prompts/context files.
- Prompt library for common patterns (CRUD, API integration, error handling).
- Multi-repo context validation across scoped repositories.

Nice-to-have deliverables:

- Custom agent definitions for Accor-specific architecture patterns.
- Developer experience survey.

Pre-requisites:

- S1 complete.
- Forked mock project available (SPA + backend + DB, multi-repo).
- AccorGPT/Claude Code configured.
- Accor coding standards provided.
- Accor engineering lead available at least 2 days/week.

Exclusions:

- Code review automation (T2).
- Test generation (T3).
- Tool selection.
- Production deployment.
- Defining standards without Accor input.

Resources: PO 10%, Tech Lead 40%, 2 Developers full-time.  
Duration: 2 weeks.

### T2: AI-Augmented Code Review

Purpose:
Set up AI-assisted code review in GitLab with suggestions, quality gates, and standards enforcement.

Must-have deliverables:

- AI-powered code review in GitLab merge request workflow.
- Quality gates enforcing coding standards.
- Review agent configuration documentation.

Nice-to-have deliverables:

- Auto-fix suggestions.
- SonarQube integration for AI-reviewed quality thresholds.

Pre-requisites:

- T1 complete.
- Forked mock project available.
- GitLab CI/CD admin access.
- SonarQube access.
- Accor DevOps engineer available at least 2 days/week.

Exclusions:

- Code generation (T1).
- Security-specific scanning (T7).
- Manual review process redesign.
- Unilateral quality gate decisions.

Resources: PO 10%, Tech Lead 40%, 2 Developers full-time.  
Duration: 2 weeks.

### T3: AI-Augmented Testing and Quality

Purpose:
Embed AI in testing: generation (unit/integration/E2E), coverage analysis, gap identification, CI triggers.

Must-have deliverables:

- AI-generated unit tests for frontend and backend.
- CI integration with test generation on merge requests.
- Coverage analysis and gap report.

Nice-to-have deliverables:

- AI-generated E2E tests (Playwright).
- AI-assisted test maintenance on code changes.
- BrowserStack/XRay integration evaluation.

Pre-requisites:

- S1 complete.
- Forked mock project available.
- GitLab CI access.
- Playwright/SonarQube/XRay access.
- Accor QA lead available at least 1 day/week.

Exclusions:

- Performance/load testing.
- Manual QA process redesign.
- Test environment provisioning.
- Finalizing test strategy without Accor QA validation.

Resources: PO 10%, Tech Lead 40%, 2 Developers full-time.  
Duration: 2 weeks.

### T4: AI-Augmented Release and Deploy

Purpose:
Embed AI in release/deployment orchestration with Accor GitFlow Terraform pipeline, feature flags, and rollback recommendations.

Must-have deliverables:

- AI-assisted deployment configurations integrated with Accor Terraform CD pipeline.
- AI-driven release workflow (pre-deploy checks, approval recommendations, go/no-go signals).
- AI-assisted rollback decision recommendations.
- Feature-flipping enablement and consistency validation across environments.
- Release notes generation from deployment diff.

Nice-to-have deliverables:

- CMDB/ServiceNow integration for change request and release tracking.
- Canary/blue-green recommendations.
- Deployment history analysis for failure patterns.
- Multi-environment promotion validation.

Pre-requisites:

- S1 complete.
- Forked mock project available.
- Access to Accor in-house Terraform CD pipeline with deployment permissions.
- Non-production AWS access.
- Feature-flag tooling access.
- Accor Platform Engineering available at least 3 days/week.

Exclusions:

- Production deployment.
- Terraform module authoring / IaC generation (T11).
- CI/CD pipeline creation / quality gate definition (T12).
- Landing zone design changes.
- Network/VPN changes.
- Migration to FluxCD/ArgoCD.

Resources: PO 10%, Tech Lead 40%, 2 Developers full-time.  
Duration: 2 weeks.

### T5: AI-Augmented Monitoring and Alerting

Purpose:
Embed AI in detection/alerting: anomaly detection, alert enrichment, noise reduction, SLO-driven signals.

Must-have deliverables:

- AI-augmented anomaly detection and incident identification (Splunk + CloudWatch).
- Automated alert enrichment with deployment/commit context.
- Alert noise reduction through filtering/correlation.
- SLO-based alerting tied to error budget risk.

Nice-to-have deliverables:

- Zabbix/ITOM correlation.
- Slack webhook integration.
- Predictive alerting.

Pre-requisites:

- S1 complete.
- Forked mock project deployed.
- Splunk/O11Y and CloudWatch access with alert write permissions.
- Monitoring dashboard access.
- Accor Ops/SRE available at least 3 days/week.

Exclusions:

- Bug triage/fix workflows (T6).
- ServiceNow integration (T10).
- Security event monitoring (T7).
- Alert rules without Accor Ops validation.

Resources: PO 10%, Tech Lead 40%, 2 Developers full-time.  
Duration: 2 weeks.

### T6: AI-Augmented Maintenance and Bug Management

Purpose:
Embed AI in bug lifecycle: triage, missing info requests, root cause pinpointing, suggested fixes.

Must-have deliverables:

- AI-powered bug triage in Jira (priority + labels).
- Automated requests for missing reproduction info.
- Code-level root cause identification.
- AI-suggested fixes for simple/recurring patterns (with review).

Nice-to-have deliverables:

- Recurring bug pattern detection.
- Toil identification and automation recommendations.
- AI-assisted technical debt prioritization.

Pre-requisites:

- S1 complete.
- T5 complete.
- Forked mock project deployed.
- Jira automation permissions.
- Accor development team available at least 2 days/week.
- Access to historical bug data.

Exclusions:

- Monitoring/alerting setup (T5).
- ServiceNow ITSM management (T10).
- Security incident response (T7).
- On-call rotation/process redesign.
- Triage rules deployment without sign-off.

Resources: PO 10%, Tech Lead 40%, 2 Developers full-time.  
Duration: 2 weeks.

### T7: AI-Augmented Security and Compliance

Purpose:
Embed AI in PDLC security checks: scan interpretation, fix suggestions, compliance docs, policy-as-code validation.

Must-have deliverables:

- AI-assisted interpretation of Checkmarx/Trivy/Wiz findings with remediation prioritization.
- Vulnerability-to-fix suggestions in merge requests.
- Security findings report with AI recommendations.
- Policy-as-code validation against security rules.

Nice-to-have deliverables:

- AI-generated compliance documentation.
- DefectDojo integration.
- Imperva WAF event correlation.

Pre-requisites:

- S1 complete.
- Forked mock project available.
- Checkmarx/Trivy/Wiz access.
- Active Accor Cybersecurity engagement at least 3 days/week.
- Existing security policies and compliance rules documented.

Exclusions:

- Penetration testing.
- Security architecture redesign.
- Vault setup.
- Compliance certification activities.
- Unit can be descoped/postponed if Cybersecurity unavailable.

Resources: PO 10%, Tech Lead 40%, 2 Developers full-time.  
Duration: 2 weeks.

### T8: AI-Augmented Code Documentation Generation

Purpose:
Embed AI in documentation workflows from code, APIs, ADRs, and freshness validation.

Must-have deliverables:

- AI-generated technical documentation (architecture, APIs, modules).
- AI-generated ADRs from changes/decisions.
- Confluence integration for automated publishing.
- Freshness validation (stale docs vs code).

Nice-to-have deliverables:

- AI-generated onboarding docs.
- Automated changelog generation.
- Diagram generation (architecture/sequence/flow).
- Documentation quality gates in CI.

Pre-requisites:

- S1 complete.
- Forked mock project available.
- Confluence publishing access.
- Existing documentation standards/templates.
- Technical writer or doc owner available at least 1 day/week.

Exclusions:

- User-facing product documentation.
- Training material creation.
- Knowledge transfer sessions (covered in S2).
- Template creation without Accor standards review.

Resources: PO 10%, Tech Lead 40%, 2 Developers full-time.  
Duration: 2 weeks.

### T9: AI-Augmented Architecture and Technical Design

Purpose:
Embed AI in design-time architecture support: solution design, impact analysis, pattern recommendations, decision support.

Must-have deliverables:

- AI-assisted solution design workflow from requirements.
- AI-powered impact analysis of proposed design changes across repos.
- Design pattern recommendations aligned with Accor conventions/constraints.
- Decision support with precedents, trade-offs, and risks.

Nice-to-have deliverables:

- Technical debt identification/classification.
- LeanIX/CMDB architecture registry integration.
- AI-assisted technology choice evaluation.
- Design pre-review automation against standards.

Pre-requisites:

- S1 complete.
- Forked mock project available.
- Confluence and/or Notion access.
- Existing architecture standards/conventions.
- Accor Solution Architect or Tech Lead available at least 2 days/week.

Exclusions:

- Redesign of Accor systems.
- Enterprise architecture governance changes.
- LeanIX landscape-level modeling.
- Unit can be descoped/postponed without architecture counterpart.

Resources: PO 10%, Tech Lead 40%, 2 Developers full-time.  
Duration: 2 weeks.

### T10: AI-Augmented ITSM and Incident Management

Purpose:
Embed AI in ITSM flow: incident creation from alerts, triage/routing, change generation, problem linking, CMDB enrichment.

Must-have deliverables:

- AI-assisted incident creation from Splunk/CloudWatch alerts to ServiceNow.
- Automated triage (severity/category/routing suggestions).
- AI-generated change requests from resolved incident patterns.
- AI-generated knowledge base entries from resolved incidents.

Nice-to-have deliverables:

- Root cause correlation to problem records.
- CMDB enrichment suggestions.
- Automated post-incident review generation.
- Predictive incident detection.

Pre-requisites:

- S1 complete.
- Forked mock project available.
- ServiceNow access (incident/change/problem/CMDB).
- T5 complete or in progress.
- Active Accor ITSM/ServiceNow engagement at least 2 days/week.
- Existing categorization and routing rules documented.

Exclusions:

- ServiceNow platform customization/development.
- ITSM process redesign/governance changes.
- CMDB data quality remediation.
- Non-ServiceNow ITSM integration.
- Unit can be descoped/postponed if ServiceNow team unavailable.

Resources: PO 10%, Tech Lead 40%, 2 Developers full-time.  
Duration: 2 weeks.

### T11: AI-Augmented Infrastructure Provisioning

Purpose:
Embed AI in IaC authoring/validation: Terraform generation, dependency analysis, refactoring, troubleshooting, shift-left compliance.

Must-have deliverables:

- AI-assisted Terraform module generation from requirements/architecture intent.
- AI-powered IaC review against Accor conventions, security policies, naming.
- Cross-stack dependency analysis before merge.
- Terraform apply troubleshooting support.

Nice-to-have deliverables:

- IaC refactoring recommendations (module extraction, DRY).
- Shift-left cost awareness.
- State operation assistance (imports/moves/removals) with safety checks.
- AI-generated infra documentation from Terraform/state.
- Migration guidance for deprecated Terraform patterns.

Pre-requisites:

- S1 complete.
- Forked mock project available.
- AWS dev/int access and Terraform state visibility.
- Existing Terraform modules and conventions.
- Active Platform Engineering/CloudOps engagement at least 2 days/week.

Exclusions:

- Production infrastructure changes.
- AWS account/org setup.
- FinOps tool implementation/configuration.
- Network architecture/security group redesign.
- Drift detection (handled by Terraform plan).
- Unit can be descoped/postponed if Platform Engineering unavailable.

Resources: PO 10%, Tech Lead 40%, 2 Developers full-time.  
Duration: 2 weeks.

### T12: AI-Augmented Pipeline Generation and Quality Gates

Purpose:
Embed AI in pipeline-as-code authoring and quality control: generation, thresholds, failure diagnosis, optimization.

Must-have deliverables:

- AI-assisted pipeline generation from project structure.
- AI-defined quality gates from codebase analysis (coverage, complexity, duplication, vulnerability counts).
- Pipeline failure diagnosis from logs with suggested fixes.
- Pipeline optimization recommendations (speed, redundancy, caching).
- Pipeline drift detection versus Accor standards.

Nice-to-have deliverables:

- Reusable pipeline template library (Java/Node.js/Python patterns).
- Quality gate evolution over project maturity.
- Cross-pipeline dependency analysis.

Pre-requisites:

- S1 complete.
- Forked mock project available.
- GitLab CI/CD pipeline editing rights.
- SonarQube access.
- Existing pipeline templates/standards.
- DevOps/CI-CD team available at least 2 days/week.

Exclusions:

- GitLab platform admin/runner management.
- SonarQube server config/rule customization.
- Production pipeline execution.
- Build tool migration.
- Unit can be descoped/postponed if DevOps unavailable.

Resources: PO 10%, Tech Lead 40%, 2 Developers full-time.  
Duration: 2 weeks.

### F1: AI-Augmented Business Requirements Gathering

Purpose:
Embed AI in requirements extraction, structuring, traceability, and change impact analysis.

Must-have deliverables:

- AI-assisted requirements extraction from transcripts/documents.
- Structured requirements repository with traceability matrix.
- AI-powered impact analysis for requirement changes.
- Requirements quality validation (completeness, consistency, testability).

Nice-to-have deliverables:

- AI-generated acceptance criteria.
- AI-generated stakeholder communication summaries and meeting minutes.
- Requirements-to-code traceability proof of concept.

Pre-requisites:

- S1 complete.
- Forked mock project available.
- Jira/Confluence access.
- Sample requirements documentation provided.
- Active BA/PO engagement at least 3 days/week.

Exclusions:

- Real-project requirements gathering.
- Business/domain expertise provision.
- Product strategy/roadmap definition (F2).
- Cannot validate tooling without Accor BA involvement.

Resources: PO 80%, Tech Lead 20%.  
Duration: 4 weeks.

### F2: AI-Augmented Product Management

Purpose:
Embed AI in product workflows: story creation, prioritization, estimation, acceptance criteria, analytics interpretation.

Must-have deliverables:

- AI-assisted epic/user story generation in Jira.
- AI-generated acceptance criteria and test scenarios.
- AI-powered effort estimation from codebase complexity.
- Backlog prioritization recommendations.

Nice-to-have deliverables:

- Roadmap scenario modeling.
- Product analytics interpretation and insight generation.
- Automated dependency mapping across epics/features.

Pre-requisites:

- S1 complete.
- Forked mock project available.
- Jira/Confluence access.
- Sample backlog provided.
- Active Accor PO engagement at least 3 days/week.

Exclusions:

- Project management processes (F3).
- Business requirements elicitation (F1).
- Product strategy definition or real product decisions.
- Cannot validate in isolation without Accor PO involvement.

Resources: PO 80%, Tech Lead 20%.  
Duration: 4 weeks.

### F3: AI-Augmented Project Management

Purpose:
Embed AI in PM workflows: sprint planning, velocity forecasting, risk detection, reporting, resource optimization.

Must-have deliverables:

- AI-assisted sprint planning (selection and capacity recommendations).
- Automated status report generation from Jira.
- AI-powered risk identification and early warning.
- Velocity forecasting and delivery prediction.

Nice-to-have deliverables:

- AI-generated stakeholder communication drafts.
- Resource allocation optimization.
- Retrospective insight extraction and action tracking.

Pre-requisites:

- S1 complete.
- Forked mock project available.
- Jira/Confluence/MS Teams access.
- Historical project data provided.
- Active Delivery/Project Manager engagement at least 3 days/week.

Exclusions:

- Product management workflows (F2).
- Actual project delivery/team management.
- PMO redesign/organizational change.
- Cannot validate PM tooling without Accor PM involvement.

Resources: PO 80%, Tech Lead 20%.  
Duration: 4 weeks.

### S2: Wrap-Up

Purpose:
Co-run one full sprint on the mock project using all AI-augmented PDLC tools; validate end-to-end flow; produce final report and handover.

Must-have deliverables:

- Full sprint execution with AI-augmented PDLC (requirement -> code -> test -> deploy -> operate).
- Capture indicative cycle timing and qualitative improvement evidence where baselines exist.
- Execution report: findings, metrics, successes, failures.
- Final handover package (configs, prompts, agents, quality gates).
- Recommendations for full-scale rollout (Transformation Phase 2 input).

Nice-to-have deliverables:

- Knowledge transfer sessions.
- Video recordings of workflows.
- Maturity assessment by PDLC stage with roadmap.

Pre-requisites:

- All relevant units complete (or explicitly descoped).
- Forked mock project fully integrated.
- Full Accor cross-functional team available for 2 weeks.
- Leadership available for sprint review and final validation.

Exclusions:

- New feature development or tool exploration.
- Organizational change management.
- Phase 2 contract negotiation.
- Sprint cannot run without Accor team participation.

Resources: 1 Product Owner, 1 Tech Lead, 4 Developers (full-time).  
Duration: 2 weeks.

---

## 4. Timeline

Base timeline:

- 6 technical units and 1 functional unit in 9 weeks.

Visual sequencing shown in source:

- Week 1: S1
- Parallel technical units distributed across Weeks 2-10
- Functional stream running in parallel
- Final wrap-up S2 at end

Timeline with additional package:

- 10 technical units and 2 functional units in 13 weeks.

---

## 5. Team Composition

Team setup roles:

- Engagement Manager
- AI Product Owner
- AI Lead
- AI Engineer
- AI Engineer
- AI Engineer
- AI Engineer

Role definitions:

### AI Lead

Responsibilities:

- Technical coordination across streams.
- Architecture decisions for AI integration patterns.
- Consistency/coherence across work units (prompts, agents, standards).
- Review/validation of technical deliverables.
- Interface with Accor engineering leadership.
- Participate in functional units (20%) for feasibility and technical support.

Key interactions:

- Engineering Lead
- Architect

### AI Engineer

Responsibilities:

- Hands-on implementation of technical work units.
- Configure AI tooling, create prompts, build agents, set up pipelines.
- Validate AI outputs against Accor standards.
- Document configurations and implementation patterns.
- Participate in S1 and S2 at full capacity.

Key interactions:

- Developers
- Platform Engineers
- QA leads
- Ops/SRE team

### AI Product Owner

Responsibilities:

- Project management (20%): planning, tracking, reporting, dependency coordination.
- Functional unit execution (80%): design and validate AI-augmented workflows with Accor stakeholders.

Key interactions:

- Business Analysts
- Product Owners
- Project Managers
- Delivery Leads

### Engagement Manager

Responsibilities:

- Overall governance.
- Risk management and escalation.
- Customer relationship management with Accor leadership.
- Monthly steering facilitation.
- Commercial and contractual oversight.
- Alignment between PALO IT delivery and Accor expectations.

Key interactions:

- Leadership

---

## 6. Pre-requisites, Assumptions, Risks, and Exclusions

### Pre-requisites (before end of S1)

- Mock project forked, sanitized, and available in GitLab.
- Isolated environments provisioned (at least dev/int).
- PALO IT accounts created (GitLab, Jira, Confluence, AWS, ServiceNow, Splunk).
- AI tool licenses allocated.
- Existing PDLC documentation and standards accessible.
- Network/VPN access available (if remote).

### Assumptions

- PALO IT delivers from Thailand unless otherwise confirmed.
- Accor provides forked sanitized mock project (SPA frontend + lightweight backend + database) before T0.
- Multi-repo structure reflects Accor real delivery pattern.
- Isolated environments provided with no production data exposure.
- All tool access granted in first week (S1).
- Mock project remains simple in business logic; complexity sits in PDLC flow.
- Named Accor counterparts stay engaged through the full engagement.
- Counterpart availability meets unit-level expectations (2-4 days/week).
- Accor leadership available for S1 prioritization and S2 final presentation.
- Existing standards/conventions/docs are provided by Accor (not authored from scratch by PALO IT).
- AI tools already selected (AccorGPT/Claude Code, Copilot); no tool evaluation in scope.
- AccorGPT (LiteLLM + Bedrock) is operational and accessible from day one.
- AI model capability assumed current-generation (for example Claude Opus/Sonnet 4.6, GPT-5.4+), no fine-tuning required.
- Data residency and AI governance are handled by Accor approved endpoints.
- Nice-to-have deliverables are best effort.
- Outputs are starting points, not production-ready.
- No production deployment or production data access is required.
- No organizational change management/training rollout/team onboarding beyond S2 knowledge transfer.

### Risks and mitigation

- Accor counterpart unavailability (High):
  - Prerequisite is explicit; units paused/deprioritized if counterpart unavailable.
- ServiceNow access/integration complexity in T10 (High):
  - Scope must-haves to incident creation + triage; deprioritize if access delayed.
- Late T0 start (Medium):
  - Reduce unit count and prioritize highest-risk units first.
- Security team engagement in T7 (High):
  - Reduce must-haves to interpretation + fix suggestions; postpone if unavailable.
- Multi-repo AI context limitations in T1 (Medium):
  - Treat as validation; document limits/workarounds rather than force resolution.
- Mock project too simple (Medium):
  - Assess in S1 and adjust scope; multi-repo is a prerequisite.
- Tool access delays (Medium):
  - Submit early; validate in S1 gate; resequence blocked units.
- AI tool evolution mid-engagement (Medium):
  - Version-pin configs and document versions used.
- Cross-stream dependencies blocking work (Low):
  - Sequence dependent units on same stream; prioritize independent units on parallel stream.
- Terraform state not accessible for T11 (Medium):
  - Work from fresh Terraform on mock project if needed.
- Accor standards undocumented (Low):
  - Capture what exists in S1; propose first draft for validation.
- KPI definition difficulties (Low):
  - Define measurable indicators in S1, including qualitative metrics where needed.

### Risk acceptance

This engagement is explicitly for de-risking.
Outcomes such as "does not work well enough yet" or "requires more investment than anticipated" are valid success outcomes if blockers are clearly identified and documented.

### Exclusions

- Production deployment or production data access.
- Tool selection/vendor evaluation.
- Custom model training/fine-tuning.
- Organizational transformation/team restructuring/process redesign.
- Full-scale rollout to Accor delivery teams.
- Integration with every tool in Accor landscape (scope confirmed during S1).
- Performance/load testing, penetration testing, or compliance certification.
- Third-party procurement/licensing/subscription management.
- Delivering any unit without active Accor counterpart involvement.
- Guaranteeing specific productivity gains (this is exploratory).

---

## Contact

Frederic Bernaroyat  
fbernaroyat@palo-it.com  
+66 805144156
