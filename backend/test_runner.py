import requests
import time
import json


BASE_URL = (
    "http://127.0.0.1:8000/generate"
)

# 10 real prompts
real_prompts = [

    "Build CRM with login contacts dashboard payments analytics",

    "Build ecommerce app with login payments",

    "Build school management system with dashboard",

    "Build admin panel with analytics",

    "Build chat app with login profile",

    "Build social media app with profile chat login",

    "Build healthcare dashboard with login",

    "Build subscription platform with payments",

    "Build employee management dashboard",

    "Build online learning platform with login"
]


# 10 edge cases
edge_cases = [

    "Build app",

    "Build payment app",

    "Build dashboard",

    "Build login",

    "Build analytics system",

    "Build social media without users",

    "Build premium app without login",

    "Build CRM but no database",

    "Build ecommerce with no payment",

    "Build random system"
]


all_prompts = (
    real_prompts
    + edge_cases
)

success_count = 0
failure_count = 0

retry_count = 0

failure_types = {}

latencies = []


print("\n")
print("=" * 60)
print("AI COMPILER EVALUATION FRAMEWORK")
print("=" * 60)
print("\n")


for prompt in all_prompts:

    payload = {
        "prompt": prompt
    }

    start_time = time.time()

    response = requests.post(
        BASE_URL,
        json=payload
    )

    end_time = time.time()

    latency = (
        end_time
        - start_time
    )

    latencies.append(
        latency
    )

    result = (
        response.json()
    )

    runtime_status = (
        result["runtime"]
        [
            "execution_status"
        ]
    )

    validation_status = (
        result["validation"]
        [
            "status"
        ]
    )

    failure_handling = (
        result[
            "failure_handling"
        ]
    )

    print("-" * 60)

    print(
        f"Prompt: {prompt}"
    )

    print(
        f"Runtime: {runtime_status}"
    )

    print(
        f"Validation: {validation_status}"
    )

    print(
        f"Latency: "
        f"{latency:.2f}s"
    )

    if (
        runtime_status
        == "SUCCESS"
    ):

        success_count += 1

    else:

        failure_count += 1

        validation_errors = (
            result
            [
                "validation"
            ]
            [
                "errors"
            ]
        )

        for error in (
            validation_errors
        ):

            if (
                error
                not in failure_types
            ):

                failure_types[
                    error
                ] = 0

            failure_types[
                error
            ] += 1

    if (
        failure_handling[
            "status"
        ]
        ==
        "needs_attention"
    ):

        retry_count += 1


total_requests = (
    len(all_prompts)
)

success_rate = (
    success_count
    /
    total_requests
) * 100

avg_latency = (
    sum(latencies)
    /
    len(latencies)
)

avg_retries = (
    retry_count
    /
    total_requests
)


metrics = {

    "total_requests":
    total_requests,

    "success_count":
    success_count,

    "failure_count":
    failure_count,

    "success_rate":
    f"{success_rate:.2f}%",

    "avg_latency":
    f"{avg_latency:.2f}s",

    "avg_retries_per_request":
    round(
        avg_retries,
        2
    ),

    "failure_types":
    failure_types
}


print("\n")
print("=" * 60)
print("FINAL METRICS")
print("=" * 60)

print(
    json.dumps(
        metrics,
        indent=4
    )
)


with open(
    "evaluation_metrics.json",
    "w"
) as file:

    json.dump(
        metrics,
        file,
        indent=4
    )

print(
    "\nSaved:"
    " evaluation_metrics.json"
)