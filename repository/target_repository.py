from returns.maybe import Maybe
from returns.result import Success, Result, Failure
from sqlalchemy.exc import SQLAlchemyError
from config.base import session_factory
from models.Targets import targets


def insert_target(target: targets) -> Result[targets, str]:
    with session_factory() as session:
        try:
            session.add(target)
            session.commit()
            session.refresh(target)
            return Success(target)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))

def find_target_by_id(target_id: int) -> Maybe[targets]:
    with session_factory() as session:
        return Maybe.from_optional(session.get(targets, target_id))

def delete_target_by_id(target_id: int) -> Result[targets, str]:
    with session_factory() as session:
        try:
            maybe_target = find_target_by_id(target_id)
            if maybe_target is Nothing:
                return Failure(f"No target found with id {target_id}")
            target = maybe_target.map(session.merge).unwrap()
            session.delete(target)
            session.commit()
            return Success(target)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))

def update_target(target_id: int, updated_target: targets) -> Result[targets, str]:
    with session_factory() as session:
        try:
            maybe_target = find_target_by_id(target_id).map(session.merge)
            if maybe_target is Nothing:
                return Failure(f"No target found with id {target_id}")
            target_to_update = maybe_target.unwrap()
            target_to_update.target_industry = updated_target.target_industry
            target_to_update.city_id = updated_target.city_id
            target_to_update.target_type_id = updated_target.target_type_id
            target_to_update.target_priority = updated_target.target_priority
            session.commit()
            session.refresh(target_to_update)
            return Success(target_to_update)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))




def get_all_targets() -> list:

    with session_factory() as session:
        try:
            all_targets = session.query(targets).all()
            return all_targets
        except SQLAlchemyError as e:
            print(f"Error retrieving targets: {e}")
            return []