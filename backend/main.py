
from runtime_simulator import simulate_runtime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from generator import (
    extract_intent,
    system_design,
    generate_schema
)
from diagram_generator import (
    generate_architecture_diagram
)
from code_generator import (
    generate_code
)
from cost_analyzer import (
    analyze_cost_quality
)
from refinement import (
    refine_system
)
from exporter import (
    export_blueprint
)
from zip_generator import (
    create_project_zip
)
from validator import (
    validate_system,
    handle_failures
)

from repair import (
    repair_system
)


app = FastAPI(
    title="AI Compiler"
)

# CORS for frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Input Model
class PromptInput(BaseModel):
    prompt: str


# Home Route
@app.get("/")
def home():
    return {
        "message":
        "AI Compiler Running"
    }

@app.post("/generate")
def generate(data: PromptInput):

    # Stage 1 → Intent Extraction
    intent = extract_intent(
        data.prompt
    )

    # Stage 2 → Failure Handling
    failure_handling = (
        handle_failures(
            intent
        )
    )

    # Stage 3 → System Design
    architecture = (
        system_design(
            intent
        )
    )

    # Stage 4 → Schema Generation
    schemas = (
        generate_schema(
            intent,
            architecture
        )
    )

    # Stage 5 → Refinement Layer
    refinement = (
        refine_system(
            intent,
            architecture,
            schemas
        )
    )

    intent = (
        refinement[
            "intent"
        ]
    )

    architecture = (
        refinement[
            "architecture"
        ]
    )

    schemas = (
        refinement[
            "schemas"
        ]
    )

    # Stage 6 → Validation
    validation = (
        validate_system(
            intent,
            architecture,
            schemas
        )
    )

    # Stage 7 → Repair
    repair = (
        repair_system(
            intent,
            architecture,
            schemas,
            validation
        )
    )

    # Stage 8 → Runtime
    runtime = (
        simulate_runtime(
            architecture,
            schemas
        )
    )

    # Stage 9 → Export
    export_result = (
        export_blueprint({

            "user_prompt":
            data.prompt,

            "intent_extraction":
            intent,

            "system_design":
            architecture,

            "schemas":
            schemas,

            "validation":
            validation,

            "failure_handling":
            failure_handling,

            "repair":
            repair,

            "runtime":
            runtime
        })
    )

    # Stage 10 → Code Generation
    generated_code = (
        generate_code(
            intent,
            architecture
        )
    )

    # Stage 11 → ZIP
    zip_result = (
        create_project_zip()
    )

    # Stage 12 → Diagram
    diagram_result = (
        generate_architecture_diagram(
            architecture
        )
    )
    # Stage 13 → Cost vs Quality
    cost_quality = (
    analyze_cost_quality()
)
    return {

        "user_prompt":
        data.prompt,

        "intent_extraction":
        intent,

        "system_design":
        architecture,

        "schemas":
        schemas,

        "validation":
        validation,

        "failure_handling":
        failure_handling,

        "repair":
        repair,

        "runtime":
        runtime,

        "export":
        export_result,

        "generated_code":
        generated_code,

        "download_project":
        zip_result,

        "architecture_diagram":
        diagram_result,

        "refinement":
        refinement,
        "cost_quality_tradeoff":
        cost_quality,

        "status":
        "stage_13_completed"
    }