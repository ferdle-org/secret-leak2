import pandas

curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer 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" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/ferdleorg/test/actions/jobs/JOB_ID/rerun
