import os

from flask_injector import FlaskInjector
from injector import Binder, inject, singleton

from authentication.application.authentication_service import AuthenticationService
from authentication.domain.user_repository import UserRepository
from authentication.infrastructure.sqlite_user_repository import SqliteUserRepository
from location.application.location_service import LocationService
from location.domain.geocoding_client import GeocodingClient
from location.domain.reverse_geocoding_client import ReverseGeocodingClient
from location.domain.search_client import SearchClient
from location.infrastructure.tomtom_geocoding_client import TomTomGeocodingClient
from location.infrastructure.tomtom_reverse_geocoding_client import TomTomReverseGeocodingClient
from location.infrastructure.tomtom_search_client import TomTomSearchClient
from offer.application.offer_service import OfferService
from offer.domain.offer_repository import OfferRepository
from offer.infrastructure.sqlite_offer_repository import SqliteOfferRepository
from reservation.domain.reservation_repository import ReservationRepository
from reservation.application.reservation_service import ReservationService


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
def provide_location_service(geocoding_client: GeocodingClient, reverse_geocoding_client: ReverseGeocodingClient,
                             search_client: SearchClient) -> LocationService:
    return LocationService(geocoding_client, reverse_geocoding_client, search_client)

@inject
def provide_reservation_service(reservation_repository: ReservationRepository, offer_repository: OfferRepository, user_repository: UserRepository) -> ReservationService:
    return ReservationService(reservation_repository, offer_repository, user_repository)


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
        SearchClient,
        to=TomTomSearchClient(api_key=api_key),
        scope=singleton
    )
    binder.bind(
        LocationService,
        to=provide_location_service,
        scope=singleton
    )


def init_di(app):
    FlaskInjector(app=app, modules=[configure])
