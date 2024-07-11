# Host
import os

host_gorest = "https://gorest.co.in/public/v2"
host_qase_io = "https://api.qase.io/v1"

# Endpoint
api_user = host_gorest + "/users"
api_user_invalid = host_gorest + "/userss"
api_result_qase_io = host_qase_io + "/result"

# Config
TOKEN_QASE_IO = os.environ.get("QASE_IO_TOKEN")
PROJECT_CODE_QASE_IO = "DPJ"
TEST_RUN_QASE_IO = "1"

# Slack
WEBHOOK = os.environ.get("WEBHOOK_SLACK")

# Netlify
URL_NETLIFY = os.environ.get("URL_NETLIFY")