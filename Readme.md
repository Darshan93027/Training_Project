# Django Blog API - One-Day Training Project

## Project Description

### Overview
Bs using Django and Django REST Framework in one day (6-8 hours). This project focuses on core Django concepts and provides a foundation for understanding Django development.

### Learning Objectives
By completing this project, you will understand:
- Django project structure and configuration
- Models, migrations, and the ORM
- Django REST Framework basics
- Authentication with tokens
- CRUD operations via API
- Basic testing
- Deployment preparation

### Technical Stack
- **Framework**: Django 4.2+
- **API**: Django REST Framework
- **Database**: Postgresql
- **Authentication**: Token Authentication (DRF built-in)
- **Testing**: Django TestCase
- **Deployment**: Docker (basic setup)

**Target Completion Time**: 6-8 hours

---

## What Needs to Be Built

### Feature 1: User Authentication (1 hour)
**Description**: Simple user registration and token-based login

**Requirements**:
- Use Django's built-in User model
- Token-based authentication
- Registration endpoint
- Login endpoint to get token

**API Endpoints**:
- Register new user (username, email, password)
- Login and receive auth token
- Get current user info (authenticated)

**Models**:
- Use Django's built-in `User` model

---

### Feature 2: Blog Posts (2 hours)
**Description**: Create, read, update, delete blog posts

**Requirements**:
- Simple Post model with basic fields
- CRUD operations via API
- Author automatically set to logged-in user
- Only authors can edit/delete their posts
- Anyone can view published posts

**API Endpoints**:
- List all posts (public)
- Create post (authenticated)
- Get single post (public)
- Update post (author only)
- Delete post (author only)

**Post Model**:
```python
Post:
  - title (CharField, max_length=200)
  - content (TextField)
  - author (ForeignKey to User)
  - created_at (DateTimeField, auto_now_add)
  - updated_at (DateTimeField, auto_now)
```

**Business Logic**:
- Auto-assign author on post creation
- Only post author can update/delete
- All posts are public for reading

---

### Feature 3: Categories (1.5 hours)
**Description**: Organize posts with categories

**Requirements**:
- Simple Category model
- Posts can belong to one category
- List posts by category
- Basic CRUD for categories

**API Endpoints**:
- List all categories
- `POST /api/categories/` - Create category (authenticated)
- `GET /api/categories/{id}/` - Get category with its posts
- `PUT /api/categories/{id}/` - Update category
- `DELETE /api/categories/{id}/` - Delete category

**Category Model**:
```python
Category:
  - name (CharField, max_length=100, unique)
  - description (TextField, blank=True)
  - created_at (DateTimeField, auto_now_add)

Post:
  - ... (existing fields)
  - category (ForeignKey to Category, null=True, blank=True)
```

---

### Feature 4: Basic Testing (1 hour)
**Description**: Write basic tests for models and API endpoints

**Requirements**:
- Test Post model creation
- Test authentication endpoints
- Test post CRUD operations
- Test permissions (author-only editing)

**Test Coverage**:
- Model tests: Post creation, string representation
- API tests: Registration, login, post creation, update, delete
- Permission tests: Non-authors cannot edit posts

---

### Feature 5: Admin Interface (30 minutes)
**Description**: Configure Django admin for content management

**Requirements**:
- Register Post and Category models
- Customize list display
- Add search and filters
- Make it easy to manage content

**Admin Features**:
- Post admin: Show title, author, category, created date; search by title
- Category admin: Show name, post count

---

### Feature 6: Basic Deployment Setup (1 hour)
**Description**: Prepare for deployment with Docker

**Requirements**:
- Create basic Dockerfile
- Create docker-compose.yml
- Environment variables configuration
- Requirements file

---

## Django Concepts Covered

### 1. Django Fundamentals (Core)
- Project setup with `django-admin startproject`
- App creation with `python manage.py startapp`
- Settings configuration (INSTALLED_APPS, DATABASES, etc.)
- URL routing with `path()` and `include()`
- Development server

### 2. Models & Database
- Model definition with Django ORM
- Field types: CharField, TextField, ForeignKey, DateTimeField
- Relationships: ForeignKey (many-to-one)
- Migrations: `makemigrations` and `migrate`
- Model methods: `__str__()`
- Django admin model registration

### 3. Django REST Framework
- Installing and configuring DRF
- Serializers: `ModelSerializer`
- ViewSets: `ModelViewSet`
- Routers: `DefaultRouter`
- Authentication: `TokenAuthentication`
- Permissions: `IsAuthenticated`, `IsAuthenticatedOrReadOnly`, custom permissions

### 4. Authentication
- Django's built-in User model
- Token authentication
- User registration
- Login/logout
- Protected endpoints

### 5. Admin Interface
- Registering models
- Customizing list display
- Adding search and filters
- Admin actions

### 6. Testing
- Django TestCase
- API testing with DRF's APITestCase
- Creating test data
- Testing authentication
- Testing permissions

### 7. Deployment Basics
- Environment variables
- Requirements management
- Docker containerization
- Basic production settings

---

## Hour-by-Hour Implementation Schedule

### Hour 1: Setup & Authentication (0:00 - 1:00)
**Tasks**:
- [ ] Install Django and DRF
- [ ] Create Django project `django-blog-api`
- [ ] Create `users` app
- [ ] Configure DRF in settings
- [ ] Create registration serializer and view
- [ ] Create login view (obtain token)
- [ ] Create user info view
- [ ] Test authentication endpoints

**Files Created**:
- `config/settings.py` (configure DRF, auth)
- `users/serializers.py`
- `users/views.py`
- `users/urls.py`
- `config/urls.py` (include users URLs)

---

### Hour 2: Blog App & Models (1:00 - 2:00)
**Tasks**:
- [ ] Create `blog` app
- [ ] Create Post model
- [ ] Create Category model
- [ ] Run migrations
- [ ] Register models in admin
- [ ] Create superuser
- [ ] Test admin interface

**Files Created**:
- `blog/models.py`
- `blog/admin.py`
- Migrations

---

### Hour 3: Post Serializers & Views (2:00 - 3:00)
**Tasks**:
- [ ] Create PostSerializer
- [ ] Create CategorySerializer
- [ ] Create PostViewSet
- [ ] Configure URL routing with routers
- [ ] Test endpoints with DRF browsable API

**Files Created**:
- `blog/serializers.py`
- `blog/views.py`
- `blog/urls.py`

---

### Hour 4: Permissions & Business Logic (3:00 - 4:00)
**Tasks**:
- [ ] Create IsAuthorOrReadOnly permission
- [ ] Apply permissions to PostViewSet
- [ ] Auto-assign author on post creation
- [ ] Test permission logic
- [ ] Add filtering by category

**Files Created**:
- `blog/permissions.py`
- Update `blog/views.py`

---

### Hour 5: Category Endpoints (4:00 - 5:00)
**Tasks**:
- [ ] Create CategoryViewSet
- [ ] Add category endpoints
- [ ] Nest posts in category detail view
- [ ] Test category CRUD operations
- [ ] Customize admin for categories

**Files Updated**:
- `blog/views.py`
- `blog/serializers.py`
- `blog/admin.py`
- `blog/urls.py`

---

### Hour 6: Testing (5:00 - 6:00)
**Tasks**:
- [ ] Write model tests for Post and Category
- [ ] Write authentication tests
- [ ] Write post CRUD tests
- [ ] Write permission tests
- [ ] Run all tests and ensure they pass

**Files Created**:
- `blog/tests.py`
- `users/tests.py`

---

### Hour 7: Polish & Documentation (6:00 - 7:00)
**Tasks**:
- [ ] Add pagination to post list
- [ ] Add ordering (newest first)
- [ ] Improve admin interface (search, filters)
- [ ] Write README with setup instructions
- [ ] Create .env.example

**Files Created/Updated**:
- `README.md`
- `.env.example`
- Update `config/settings.py` for pagination

---

### Hour 8: Deployment Preparation (7:00 - 8:00)
**Tasks**:
- [ ] Create requirements.txt
- [ ] Create Dockerfile
- [ ] Create docker-compose.yml
- [ ] Test Docker build
- [ ] Document deployment steps

**Files Created**:
- `requirements.txt`
- `Dockerfile`
- `docker-compose.yml`
- `.gitignore`

---

## Complete API Specification

### Base URL
```
http://localhost:8000/api/
```

### Authentication
All authenticated requests must include:
```
Authorization: Token <your-token-here>
```

### Endpoints

#### Authentication Endpoints
```
POST   /api/auth/register/     - Register new user
POST   /api/auth/login/        - Login and get token
GET    /api/auth/user/         - Get current user (requires auth)
```

#### Blog Post Endpoints
```
GET    /api/posts/             - List all posts
POST   /api/posts/             - Create post (requires auth)
GET    /api/posts/{id}/        - Get single post
PUT    /api/posts/{id}/        - Update post (author only)
DELETE /api/posts/{id}/        - Delete post (author only)
```

#### Category Endpoints
```
GET    /api/categories/        - List all categories
POST   /api/categories/        - Create category (requires auth)
GET    /api/categories/{id}/   - Get category with posts
PUT    /api/categories/{id}/   - Update category (requires auth)
DELETE /api/categories/{id}/   - Delete category (requires auth)
```
## Required Dependencies

### requirements.txt
```txt
Django==4.2.8
djangorestframework==3.14.0
python-decouple==3.8
```

### Optional (for deployment)
```txt
gunicorn==21.2.0
whitenoise==6.6.0
psycopg2-binary==2.9.9
```

---

## Implementation Checklist

### Setup (15 minutes)
- [ ] Install Python 3.8+
- [ ] Create virtual environment
- [ ] Install Django and DRF
- [ ] Create Django project
- [ ] Create apps (users, blog)
- [ ] Configure settings
- [ ] Run initial migrations

### Users App (45 minutes)
- [ ] Create registration serializer
- [ ] Create user serializer
- [ ] Create registration view
- [ ] Create login view (obtain auth token)
- [ ] Create user detail view
- [ ] Configure URLs
- [ ] Test with Postman/curl

### Blog Models (30 minutes)
- [ ] Create Category model
- [ ] Create Post model
- [ ] Add `__str__` methods
- [ ] Make migrations
- [ ] Apply migrations
- [ ] Test in Django shell

### Blog API (60 minutes)
- [ ] Create CategorySerializer
- [ ] Create PostSerializer (with nested author and category)
- [ ] Create CategoryViewSet
- [ ] Create PostViewSet
- [ ] Configure routers
- [ ] Test browsable API

### Permissions (30 minutes)
- [ ] Create IsAuthorOrReadOnly permission class
- [ ] Apply to PostViewSet
- [ ] Override `perform_create` to set author
- [ ] Test permission logic

### Admin Interface (20 minutes)
- [ ] Register Post model with customization
- [ ] Register Category model with customization
- [ ] Add list_display, search_fields, list_filter
- [ ] Create superuser
- [ ] Test admin functionality

### Testing (60 minutes)
- [ ] Test Post model
- [ ] Test Category model
- [ ] Test user registration
- [ ] Test user login
- [ ] Test post creation
- [ ] Test post update (author only)
- [ ] Test post deletion (author only)
- [ ] Run tests: `python manage.py test`

### Polish (30 minutes)
- [ ] Add pagination (10 items per page)
- [ ] Add ordering (newest first)
- [ ] Add basic filtering
- [ ] Test all endpoints

### Documentation (20 minutes)
- [ ] Write README with:
  - Project description
  - Setup instructions
  - API endpoints
  - Example requests
- [ ] Create .env.example
- [ ] Add comments to code

### Deployment Prep (40 minutes)
- [ ] Create requirements.txt
- [ ] Create Dockerfile
- [ ] Create docker-compose.yml
- [ ] Create .gitignore
- [ ] Test Docker build

---

## Success Criteria

By the end of the day, the trainee should have:

### Working Features
- ✅ User registration and authentication system
- ✅ Token-based API authentication
- ✅ CRUD operations for blog posts
- ✅ CRUD operations for categories
- ✅ Author-only editing permissions
- ✅ Django admin interface for content management
- ✅ Basic tests covering main functionality

### Technical Understanding
- ✅ How Django projects and apps are structured
- ✅ How to create models and run migrations
- ✅ How to build REST APIs with DRF
- ✅ How serializers work
- ✅ How to implement authentication and permissions
- ✅ How to write basic tests
- ✅ How to use Django admin

### Deliverables
- ✅ Working Django API with ~10 endpoints
- ✅ 2 Django apps (users, blog)
- ✅ 2 models (Post, Category)
- ✅ Basic test suite
- ✅ Docker configuration
- ✅ README documentation

---

## Extension Ideas (Beyond One Day)

1. **Add Comments** (1-2 hours)
   - Create Comment model
   - Add comment endpoints
   - Nested comments under posts

2. **Add Search** (30 minutes)
   - Search posts by title and content
   - Use DRF's SearchFilter

3. **Add Filtering** (30 minutes)
   - Filter posts by category
   - Filter posts by author
   - Use django-filter

4. **Add Tags** (1 hour)
   - Create Tag model
   - ManyToMany relationship with Post
   - Tag CRUD endpoints

5. **Improve Tests** (1 hour)
   - Increase test coverage
   - Add integration tests
   - Test edge cases

6. **Deploy to Cloud** (2-3 hours)
   - Deploy to Heroku or Railway
   - Configure PostgreSQL
   - Set up production settings


**Remember**: The goal is to understand Django fundamentals, not to build a production-ready application. Focus on learning the concepts, and don't worry about making it perfect!
