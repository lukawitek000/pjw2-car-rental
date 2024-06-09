import os

from flask_injector import FlaskInjector
from injector import Binder, inject, singleton

from authentication.application.authentication_service import AuthenticationService
from authentication.domain.user_repository import UserRepository
from authentication.infrastructure.sqlite_user_repository import SqliteUserRepository
from location.application.location_service import LocationService
from location.domain.geocoding_client import GeocodingClient
from location.domain.reverse_geocoding_client import ReverseGeocodingClient
from location.infrastructure.tomtom_geocoding_client import TomTomGeocodingClient
from location.infrastructure.tomtom_reverse_geocoding_client import TomTomReverseGeocodingClient
from offer.application.offer_service import OfferService
from offer.domain.offer_repository import OfferRepository
from offer.infrastructure.sqlite_offer_repository import SqliteOfferRepository


@inject
def provide_offer_service(offer_repository: OfferRepository, user_repository: UserRepository) -> OfferService:
    return OfferService(offer_repository, user_repository)


@inject
def provide_authentication_service(user_repository: UserRepository) -> AuthenticationService:
    return AuthenticationService(user_repository)


@inject
def provide_user_repository() -> UserRepository:
    return SqliteUserRepository()


@inject
def provide_location_service(geocoding_client: GeocodingClient, reverse_geocoding_client: ReverseGeocodingClient) -> LocationService:
    return LocationService(geocoding_client, reverse_geocoding_client)


def configure(binder: Binder):
    api_key = os.getenv("TOMTOM_API_KEY")
    binder.bind(
        UserRepository,
        to=provide_user_repository,
        scope=singleton
    )
    binder.bind(
        AuthenticationService,
        to=provide_authentication_service,
        scope=singleton
    )
    binder.bind(
        OfferRepository,
        to=SqliteOfferRepository(),
        scope=singleton
    )
    binder.bind(
        OfferService,
        to=provide_offer_service,
        scope=singleton
    )
    binder.bind(
        GeocodingClient,
        to=TomTomGeocodingClient(api_key=api_key),
        scope=singleton
    )
    binder.bind(
        ReverseGeocodingClient,
        to=TomTomReverseGeocodingClient(api_key=api_key),
        scope=singleton
    )
    binder.bind(
        LocationService,
        to=provide_location_service,
        scope=singleton
    )


def init_di(app):
    FlaskInjector(app=app, modules=[configure])
