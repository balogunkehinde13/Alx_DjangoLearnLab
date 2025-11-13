# Permissions and Groups Setup

## Custom Permissions
Defined in `Article` model:
- can_view: Allows viewing of articles
- can_create: Allows creation of new articles
- can_edit: Allows editing of existing articles
- can_delete: Allows deletion of articles

## Groups
- **Viewers** → can_view
- **Editors** → can_create, can_edit
- **Admins** → all permissions

Run `python manage.py init_groups` to create groups and assign permissions automatically.

## Enforcement
Each view uses Django’s `@permission_required` decorator to restrict access.
