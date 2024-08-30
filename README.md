# Philippines Address Management

This Django app provides models to manage and store hierarchical address information in the Philippines, including Regions, Provinces, Municipalities, and Barangays.

## Models Overview

### 1. **Region**
- Represents a region in the Philippines.
- **Fields**:
  - `name`: The name of the region.
  - `psgc_code`: The Philippine Standard Geographic Code for the region.
  - `reg_code`: A unique code for the region.
  - `country`: The country the region belongs to (default is "Philippines").
  
- **Relationships**:
  - Linked to the `Province` model.

### 2. **Province**
- Represents a province within a region in the Philippines.
- **Fields**:
  - `name`: The name of the province.
  - `psgc_code`: The Philippine Standard Geographic Code for the province.
  - `prov_code`: A unique code for the province.
  - `reg_code`: The region code to which the province belongs.
  
- **Relationships**:
  - Linked to the `Region` and `Municipality` models.

### 3. **Municipality**
- Represents a municipality within a province in the Philippines.
- **Fields**:
  - `name`: The name of the municipality.
  - `psgc_code`: The Philippine Standard Geographic Code for the municipality.
  - `city_mun_code`: A unique code for the municipality.
  - `prov_code`: The province code to which the municipality belongs.
  - `reg_code`: The region code to which the municipality belongs.
  
- **Relationships**:
  - Linked to the `Province` and `Barangay` models.

### 4. **Barangay**
- Represents a barangay (smallest administrative division) within a municipality in the Philippines.
- **Fields**:
  - `name`: The name of the barangay.
  - `brgy_code`: A unique code for the barangay.
  - `city_mun_code`: The municipality code to which the barangay belongs.
  - `prov_code`: The province code to which the barangay belongs.
  - `reg_code`: The region code to which the barangay belongs.
  
- **Relationships**:
  - Linked to the `Municipality` model.

### 5. **PhAddress**
- Represents a full address in the Philippines, including the hierarchical structure from region down to barangay.
- **Fields**:
  - `country`: The country the address belongs to (default is "Philippines").
  - `unit_home_street`: Detailed street address, unit number, or home information.
  - `zip_code`: Postal code.
  - `district_id`: An optional district identifier.
  - `created_at`: Timestamp when the address was created.
  - `updated_at`: Timestamp when the address was last updated.
  
- **Relationships**:
  - Linked to the `Region`, `Province`, `Municipality`, and `Barangay` models.

## Usage

### Installation

To include this app in your Django project:

1. Add `phil_loc` to `INSTALLED_APPS` in your `settings.py`.

2. Run migrations to create the necessary database tables:

   ```bash
   python manage.py migrate
   ```
   
3. Data seeding
  ```bash
  python manage.py seed_ph_locations
  ```

### Example Usage

```python
from phil_loc.models import PhAddress

# Create a new address
address = PhAddress.objects.create(
    country='PH',
    region=region_instance,
    province=province_instance,
    municipality=municipality_instance,
    barangay_district=barangay_instance,
    unit_home_street='123 Example Street',
    zip_code=1234
)
```

## License

This project is licensed under the MIT License.

---

This `README` gives an overview of the models, their fields, and relationships, and provides a basic usage example for the `PhAddress` model. Adjust the `phil_loc` placeholders and add any additional information as needed for your specific application.