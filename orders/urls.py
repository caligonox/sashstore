from django.urls import path

from orders.views import (
    CancelledTemplateView,
    OrderCreateView,
    OrderListView,
    SuccessTemplateView,
)

app_name = "orders"

urlpatterns = [
    path("order_create/", OrderCreateView.as_view(), name="order_create"),
    path("", OrderListView.as_view(), name="orders_list"),
    path(
        "order_success/", SuccessTemplateView.as_view(), name="order_success"
    ),
    path(
        "order_cancelled/",
        CancelledTemplateView.as_view(),
        name="order_cancelled",
    ),
]
