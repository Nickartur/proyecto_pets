from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("nueva", views.v_nueva, name="nueva"),
    path("lista", views.v_lista, name="lista"),
<<<<<<< HEAD
    #path("reporte", views.v_reporte, name="reporte")
=======
>>>>>>> abbb39cf52e16b9ac26b683b2b9ea291a227728f
    path("reporte_xls", views.v_reporte, name="reporte"),
    path("reporte_pdf", views.v_generar_pdf, name="reporte_pdf")
]