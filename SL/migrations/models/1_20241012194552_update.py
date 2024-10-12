from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `course` ADD `addr` VARCHAR(32) NOT NULL  COMMENT '教室' DEFAULT '';
        ALTER TABLE `course` MODIFY COLUMN `teacher_id` INT NOT NULL  COMMENT '担任';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `course` DROP COLUMN `addr`;
        ALTER TABLE `course` MODIFY COLUMN `teacher_id` INT NOT NULL;"""
