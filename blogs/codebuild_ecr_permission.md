- 266601397973是本账户账号
>```
>{
>    "Version": "2012-10-17",
>    "Statement": [
>        {
>            "Sid": "VisualEditor0",
>            "Effect": "Allow",
>            "Action": [
>                "ecr:BatchGetImage",
>                "ecr:BatchCheckLayerAvailability",
>                "ecr:CompleteLayerUpload",
>                "ecr:DescribeImages",
>                "ecr:DescribeRepositories",
>                "ecr:GetDownloadUrlForLayer",
>                "ecr:InitiateLayerUpload",
>                "ecr:ListImages",
>                "ecr:PutImage",
>                "ecr:UploadLayerPart"
>            ],
>            "Resource": "arn:aws:ecr:*:266601397973:repository/*"
>        },
>        {
>            "Sid": "VisualEditor1",
>            "Effect": "Allow",
>            "Action": "ecr:GetAuthorizationToken",
>            "Resource": "*"
>        }
>    ]
>}
>```