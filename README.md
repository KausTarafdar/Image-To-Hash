# Image Hash API
This is a Django RESTful API that accepts a public image URL, calculates the MD5 hash and pHash of the image, and stores the data in a database. It also provides full CRUD operations for managing the stored image records.
____
### Features
- **Upload Image URL**: Submit an image URL to calculate MD5 and pHash values.
- **CRUD Operations**:
    - Create a new image record.
    - Retrieve all stored records or a specific one.
    - Update specific fields (PATCH) or the entire record (PUT).
    - Delete records.
- Hash Calculation:
    - MD5 Hash: Ensures data integrity.
    - pHash: Perceptual hash for image similarity detection.
____
### Prerequisites
- Python 3.8+
- pip package manager
____
### Installation
1. Clone the repository:
```bash
git clone <repository-url>
cd image_api_project
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install dependencies:
```bash
pip install django djangorestframework pillow imagehash requests
```
4. Run database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Start the Django server:
```bash
python manage.py runserver
```
____
### API Endpoints
1. **Create Image Record**
    - URL: /api/images/create/
    - Method: POST
    - Request Body:
    ```json
    {
        "image_url": "https://example.com/image.jpg"
    }
    ```
    - Response expected:
    ```json
    {
        "id": 1,
        "image_url": "https://example.com/image.jpg",
        "md5_hash": "d41d8cd98f00b204e9800998ecf8427e",
        "phash": "e9c6e06e30c30c4f"
    }
    ```
2. **List All Image Records**
    - URL: /api/images/
    - Method: GET
    - Response:
    ```json
    [
        {
            "id": 1,
            "image_url": "https://example.com/image.jpg",
            "md5_hash": "d41d8cd98f00b204e9800998ecf8427e",
            "phash": "e9c6e06e30c30c4f"
        }
    ]
    ```
3. **Retrieve Single Record**
    - URL: /api/images/<id>/
    - Method: GET
    - Response:
    ```json
    {
        "id": 1,
        "image_url": "https://example.com/image.jpg",
        "md5_hash": "d41d8cd98f00b204e9800998ecf8427e",
        "phash": "e9c6e06e30c30c4f"
    }
    ```
4. **Update Image Record (Partial Update)**
    - URL: /api/images/<id>/
    - Method: PATCH
    - Request Body:
    ```json
    {
        "image_url": "https://updated-example.com/image.jpg"
    }
    ```
    - Response:
    ```json
    {
        "id": 1,
        "image_url": "https://updated-example.com/image.jpg",
        "md5_hash": "d41d8cd98f00b204e9800998ecf8427e",
        "phash": "e9c6e06e30c30c4f"
    }
    ```
5. **Delete Image Record**
    - URL: /api/images/<id>/
    - Method: DELETE
    - Response:
    ```json
    {
        "message": "Record deleted successfully"
    }
    ```
___
### Technologies Used
- **Django**: Web framework.
- **Django REST Framework**: API development.
- **Pillow**: Image processing.
- **imagehash**: Perceptual hashing.
- **Requests**: HTTP requests for image download.