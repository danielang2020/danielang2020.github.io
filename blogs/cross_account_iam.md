- ECR Repo Permission
>```
>{
>  "Version": "2008-10-17",
>  "Statement": [
>    {
>      "Sid": "CrossAccountPermission",
>      "Effect": "Allow",
>      "Principal": {
>        "AWS": "arn:aws:iam::621523765256:root"
>      },
>      "Action": [
>        "ecr:BatchGetImage",
>        "ecr:GetDownloadUrlForLayer"
>      ]
>    },
>    {
>      "Sid": "LambdaECRImageCrossAccountRetrievalPolicy",
>      "Effect": "Allow",
>      "Principal": {
>        "Service": "lambda.amazonaws.com"
>      },
>      "Action": [
>        "ecr:BatchGetImage",
>        "ecr:GetDownloadUrlForLayer"
>      ],
>      "Condition": {
>        "StringLike": {
>          "aws:sourceARN": "arn:aws:lambda:*:621523765256:function:*"
>        }
>      }
>    }
>  ]
>}

- S3
>```
>{
>            "Sid": "Stmt1676032956666",
>            "Effect": "Allow",
>            "Principal": {
>                "AWS": "arn:aws:iam::621523765256:root"
>            },
>            "Action": [
>                "s3:GetObject",
>                "s3:ListBucket"
>            ],
>            "Resource": [
>                "arn:aws:s3:::quotap-cloudformation-template",
>                "arn:aws:s3:::quotap-cloudformation-template/*"
>            ]
>        }
>```

- CodeBuild ECR IAM Policy
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