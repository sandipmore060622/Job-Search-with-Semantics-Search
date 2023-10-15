
indexMapping = {
    "properties": {
        "jobpost": {
            "type": "text"
        },
    
        "Title": {
            "type": "text"
        },
        "Company": {
            "type": "text"
        },
        "AnnouncementCode": {
            "type": "keyword"
        },
        "Term": {
            "type": "keyword"
        },
        "Eligibility": {
            "type": "text"
        },
        "Audience": {
            "type": "text"
        },

        "Duration": {
            "type": "text"
        },
        "Location": {
            "type": "text"
        },
        "JobDescription": {
            "type": "text"
        },
        "JobRequirment": {
            "type": "text"
        },
        "RequiredQual": {
            "type": "text"
        },
        "Salary": {
            "type": "text"
        },
        "ApplicationP": {
            "type": "text"
        },
 
        "Notes": {
            "type": "text"
        },
        "AboutC": {
            "type": "text"
        },
        "Attach": {
            "type": "text"
        },
        "Year": {
            "type": "integer"
        },
        "Month": {
            "type": "integer"
        },
        "IT": {
            "type": "boolean"
        },
        "JobID": {
            "type": "long"
        },
        "DescriptionVector":{
            "type":"dense_vector",
            "dims": 768,
            "index":True,
            "similarity": "l2_norm"
        }
    }
}
