- ECR
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